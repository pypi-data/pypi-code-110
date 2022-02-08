# Copyright 2021 Xanadu Quantum Technologies Inc.

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
Helper functions for serializing quantum tapes.
"""
from typing import List, Tuple

import numpy as np
from pennylane import (
    BasisState,
    Hadamard,
    Projector,
    QubitStateVector,
    Rot,
)
from pennylane.grouping import is_pauli_word
from pennylane.operation import Observable, Tensor
from pennylane.tape import QuantumTape

try:
    from .lightning_qubit_ops import (
        StateVectorC64,
        ObsStructC64,
        StateVectorC128,
        ObsStructC128,
        DEFAULT_KERNEL_FOR_OPS,
    )
except ImportError:
    pass


def _is_lightning_gate(gate_name):
    """Returns True if the gate (besides Matrix) is implemented
    and exported from lightning.

    Args:
        gate_name (str): the name of gate
    """
    if gate_name == "Matrix":
        return False
    return gate_name in DEFAULT_KERNEL_FOR_OPS


def _obs_has_kernel(obs: Observable) -> bool:
    """Returns True if the input observable has a supported kernel in the C++ backend.

    Args:
        obs (Observable): the input observable

    Returns:
        bool: indicating whether ``obs`` has a dedicated kernel in the backend
    """
    if is_pauli_word(obs):
        return True
    if isinstance(obs, (Hadamard, Projector)):
        return True
    if isinstance(obs, Tensor):
        return all(_obs_has_kernel(o) for o in obs.obs)
    return False


def _serialize_obs(tape: QuantumTape, wires_map: dict, use_csingle: bool = False) -> List:
    """Serializes the observables of an input tape.

    Args:
        tape (QuantumTape): the input quantum tape
        wires_map (dict): a dictionary mapping input wires to the device's backend wires
        use_csingle (bool): whether to use np.complex64 instead of np.complex128

    Returns:
        list(ObsStructC128 or ObsStructC64): A list of observable objects compatible with the C++ backend
    """
    obs = []

    if use_csingle:
        ctype = np.complex64
        obs_py = ObsStructC64
    else:
        ctype = np.complex128
        obs_py = ObsStructC128

    for o in tape.observables:
        is_tensor = isinstance(o, Tensor)

        wires = []

        if is_tensor:
            for o_ in o.obs:
                wires_list = o_.wires.tolist()
                w = [wires_map[w] for w in wires_list]
                wires.append(w)
        else:
            wires_list = o.wires.tolist()
            w = [wires_map[w] for w in wires_list]
            wires.append(w)

        name = o.name if is_tensor else [o.name]

        params = []

        if not _obs_has_kernel(o):
            if is_tensor:
                for o_ in o.obs:
                    if not _obs_has_kernel(o_):
                        params.append(o_.matrix.ravel().astype(ctype))
                    else:
                        params.append([])
            else:
                params.append(o.matrix.ravel().astype(ctype))

        ob = obs_py(name, params, wires)
        obs.append(ob)

    return obs


def _serialize_ops(
    tape: QuantumTape, wires_map: dict, use_csingle: bool = False
) -> Tuple[List[List[str]], List[np.ndarray], List[List[int]], List[bool], List[np.ndarray]]:
    """Serializes the operations of an input tape.

    The state preparation operations are not included.

    Args:
        tape (QuantumTape): the input quantum tape
        wires_map (dict): a dictionary mapping input wires to the device's backend wires
        use_csingle (bool): whether to use np.complex64 instead of np.complex128

    Returns:
        Tuple[list, list, list, list, list]: A serialization of the operations, containing a list
        of operation names, a list of operation parameters, a list of observable wires, a list of
        inverses, and a list of matrices for the operations that do not have a dedicated kernel.
    """
    names = []
    params = []
    wires = []
    inverses = []
    mats = []

    sv_py = StateVectorC64 if use_csingle else StateVectorC128

    uses_stateprep = False

    for o in tape.operations:
        if isinstance(o, (BasisState, QubitStateVector)):
            uses_stateprep = True
            continue
        elif isinstance(o, Rot):
            op_list = o.expand().operations
        else:
            op_list = [o]

        for single_op in op_list:
            is_inverse = single_op.inverse

            name = single_op.name if not is_inverse else single_op.name[:-4]
            names.append(name)

            if not _is_lightning_gate(name):
                params.append([])
                mats.append(single_op.matrix)

                if is_inverse:
                    is_inverse = False
            else:
                params.append(single_op.parameters)
                mats.append([])

            wires_list = single_op.wires.tolist()
            wires.append([wires_map[w] for w in wires_list])
            inverses.append(is_inverse)

    return (names, params, wires, inverses, mats), uses_stateprep
