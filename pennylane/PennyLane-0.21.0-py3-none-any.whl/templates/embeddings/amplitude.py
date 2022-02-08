# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""
Contains the AmplitudeEmbedding template.
"""
# pylint: disable-msg=too-many-branches,too-many-arguments,protected-access
import numpy as np

import pennylane as qml
from pennylane.operation import Operation, AnyWires
from pennylane.ops import QubitStateVector
from pennylane.wires import Wires

# tolerance for normalization
TOLERANCE = 1e-10


class AmplitudeEmbedding(Operation):
    r"""Encodes :math:`2^n` features into the amplitude vector of :math:`n` qubits.

    By setting ``pad_with`` to a real or complex number, ``features`` is automatically padded to dimension
    :math:`2^n` where :math:`n` is the number of qubits used in the embedding.

    To represent a valid quantum state vector, the L2-norm of ``features`` must be one.
    The argument ``normalize`` can be set to ``True`` to automatically normalize the features.

    If both automatic padding and normalization are used, padding is executed *before* normalizing.

    .. note::

        On some devices, ``AmplitudeEmbedding`` must be the first operation of a quantum circuit.

    .. warning::

        At the moment, the ``features`` argument is **not differentiable** when using the template, and
        gradients with respect to the features cannot be computed by PennyLane.

    Args:
        features (tensor_like): input tensor of dimension ``(2^n,)``, or less if `pad_with` is specified
        wires (Iterable): wires that the template acts on
        pad_with (float or complex): if not None, the input is padded with this constant to size :math:`2^n`
        normalize (bool): whether to automatically normalize the features

    Example:

        Amplitude embedding encodes a normalized :math:`2^n`-dimensional feature vector into the state
        of :math:`n` qubits:

        .. code-block:: python

            import pennylane as qml

            dev = qml.device('default.qubit', wires=2)

            @qml.qnode(dev)
            def circuit(f=None):
                qml.AmplitudeEmbedding(features=f, wires=range(2))
                return qml.expval(qml.PauliZ(0))

            circuit(f=[1/2, 1/2, 1/2, 1/2])

        The final state of the device is - up to a global phase - equivalent to the input passed to the circuit:

        >>> dev.state
        [0.5+0.j 0.5+0.j 0.5+0.j 0.5+0.j]

        **Differentiating with respect to the features**

        Due to non-trivial classical processing to construct the state preparation circuit,
        the features argument is in general **not differentiable**.

        **Normalization**

        The template will raise an error if the feature input is not normalized.
        One can set ``normalize=True`` to automatically normalize it:

        .. code-block:: python

            @qml.qnode(dev)
            def circuit(f=None):
                qml.AmplitudeEmbedding(features=f, wires=range(2), normalize=True)
                return qml.expval(qml.PauliZ(0))

            circuit(f=[15, 15, 15, 15])

        >>> dev.state
        [0.5 + 0.j, 0.5 + 0.j, 0.5 + 0.j, 0.5 + 0.j]

        **Padding**

        If the dimension of the feature vector is smaller than the number of amplitudes,
        one can automatically pad it with a constant for the missing dimensions using the ``pad_with`` option:

        .. code-block:: python

            from math import sqrt

            @qml.qnode(dev)
            def circuit(f=None):
                qml.AmplitudeEmbedding(features=f, wires=range(2), pad_with=0.)
                return qml.expval(qml.PauliZ(0))

            circuit(f=[1/sqrt(2), 1/sqrt(2)])

        >>> dev.state
        [0.70710678 + 0.j, 0.70710678 + 0.j, 0.0 + 0.j, 0.0 + 0.j]

    """

    num_wires = AnyWires
    grad_method = None

    def __init__(self, features, wires, pad_with=None, normalize=False, do_queue=True, id=None):

        wires = Wires(wires)
        self.pad_with = pad_with
        self.normalize = normalize

        features = self._preprocess(features, wires, pad_with, normalize)
        super().__init__(features, wires=wires, do_queue=do_queue, id=id)

    @property
    def num_params(self):
        return 1

    def adjoint(self):  # pylint: disable=arguments-differ
        return qml.adjoint(qml.MottonenStatePreparation)(self.parameters[0], wires=self.wires)

    def expand(self):

        with qml.tape.QuantumTape() as tape:
            QubitStateVector(self.parameters[0], wires=self.wires)

        return tape

    @staticmethod
    def _preprocess(features, wires, pad_with, normalize):
        """Validate and pre-process inputs as follows:

        * If features is batched, the processing that follows is applied to each feature set in the batch.
        * Check that the features tensor is one-dimensional.
        * If pad_with is None, check that the first dimension of the features tensor
          has length :math:`2^n` where :math:`n` is the number of qubits. Else check that the
          first dimension of the features tensor is not larger than :math:`2^n` and pad features
          with value if necessary.
        * If normalize is false, check that first dimension of features is normalised to one. Else, normalise the
          features tensor.
        """

        # check if features is batched
        batched = len(qml.math.shape(features)) > 1

        features_batch = features if batched else [features]

        # apply pre-processing to each features tensor in the batch
        for i, feature_set in enumerate(features_batch):
            shape = qml.math.shape(feature_set)

            # check shape
            if len(shape) != 1:
                raise ValueError(f"Features must be a one-dimensional tensor; got shape {shape}.")

            n_features = shape[0]
            if pad_with is None and n_features != 2 ** len(wires):
                raise ValueError(
                    f"Features must be of length {2 ** len(wires)}; got length {n_features}. "
                    f"Use the 'pad_with' argument for automated padding."
                )

            if pad_with is not None and n_features > 2 ** len(wires):
                raise ValueError(
                    f"Features must be of length {2 ** len(wires)} or "
                    f"smaller to be padded; got length {n_features}."
                )

            # pad
            if pad_with is not None and n_features < 2 ** len(wires):
                padding = [pad_with] * (2 ** len(wires) - n_features)
                feature_set = qml.math.concatenate([feature_set, padding], axis=0)

            # normalize
            norm = qml.math.sum(qml.math.abs(feature_set) ** 2)

            if qml.math.is_abstract(norm):
                if normalize or pad_with:
                    feature_set = feature_set / qml.math.sqrt(norm)

            elif not qml.math.allclose(norm, 1.0, atol=TOLERANCE):
                if normalize or pad_with:
                    feature_set = feature_set / qml.math.sqrt(norm)
                else:
                    raise ValueError(
                        f"Features must be a vector of norm 1.0; got norm {norm}."
                        "Use 'normalize=True' to automatically normalize."
                    )

            features_batch[i] = feature_set

        return qml.math.cast(features_batch if batched else features_batch[0], np.complex128)
