#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019-2021, INRIA
#
# This file is part of Openwind.
#
# Openwind is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Openwind is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openwind.  If not, see <https://www.gnu.org/licenses/>.
#
# For more informations about authors, see the CONTRIBUTORS file

"""
Delayed evaluation and differentiation of parameters.

In the context of optimization, equation coefficients must be evaluated
and differentiated for various values of parameters (such as tube length,
hole position, etc.).

These classes allows delayed evaluation of the shape parameters, as well as
their differentiation with respect to the optimization variables.
"""

from abc import ABC, abstractmethod

import numpy as np


def eval_(params):
    """
    Evaluate a list of :py:class:`DesignParameter<DesignParameter>`.

    Parameters
    ----------
    params : list of :py:class:`DesignParameter<DesignParameter>`

    Returns
    -------
    list of float
        The values of each parameter.

    """
    return [p.get_value() for p in params]

def diff_(params, diff_index):
    """
    Differentiate a list of :py:class:`DesignParameter<DesignParameter>`.

    Parameters
    ----------
    params : list of :py:class:`DesignParameter<DesignParameter>`
    diff_index : int
        Index of the optimized parameter considered for the differentiation

    Returns
    -------
    list of float
        The values of the differentiation of each parameter w.r. to the
        designated optimized parameter.

    """
    return [p.get_differential(diff_index) for p in params]


class OptimizationParameters:
    """Manage the variable parameters for optimization.

    All the variable parameters possibly modified during the optimization
    process are associated to one value of a optimized parameter list.


    Attributes
    ----------
    values : list of float
        The value associated to each parameter
    labels : list of string
        The label of each parameter
    active : list of bool
        If the parameter is include (True) or not (False) in the optimization
        process
    geom_value : list of :py:meth:`get_value \
        <openwind.design.design_parameter.DesignParameter.get_value>`
        The methods used to compute the geometric value of the parameters from
        the value stored in the :py:attr:`values<OptimizationParameters.values>` list.
    bounds : list of tuple of 2 floats
        The bounds for each parameter.
    """

    MARGIN = 1e-7
    """ margin added to the bounds to guarantee their respect"""

    def __init__(self):
        self.values = list()
        self.labels = list()
        self.active = list()
        self.geom_values = list()
        self.bounds = list()

    def __str__(self):
        msg = ('{:20s}| {:>12s} || {:>10s} < {:>12s} < {:<10s} |'
               ' {:>6s}\n'.format('Labels', 'Geom.Values', 'Min',
                                  'Optim.Values', 'Max', 'Active'))
        msg += '-'*85 + '\n'
        for k in range(len(self.labels)):
            lb, ub = self.bounds[k]
            msg += ('{:20s}| {:12.5e} || {:10.3g} < {:12.5e} < {:<10.3g} |'
                    ' {:}\n').format(self.labels[k],
                                     self.get_geometric_values()[k],
                                     lb, self.values[k], ub, self.active[k])
        return msg

    def __repr__(self):
        return "<{class_}: {labels}>".format(class_=type(self).__name__,
                                             labels=self.labels)

    def new_param(self, value, label, get_geom_values,
                  bounds=(-np.inf, np.inf)):
        """
        Add a new optimized parameter.

        Parameters
        ----------
        value : float
            The initial value associated to the new parameter.
        label : str
            The label of the new parameter.
        get_geom_values : :py:meth:`get_value \ <openwind.design.design_parameter.DesignParameter.get_value>`
            The method used to compute the geometric value of the parameter
            from its stored value.
        bounds : tuple of two floats, optional
            The bounds associated to the new parameters: (min, max).
            The default value is no bounds: (-inf, inf).

        Returns
        -------
        new_index : int
            The index at which is stored this parameters in the lists of the
            py:class:`OptimizationParameters<OptimizationParameters>` object.

        """
        new_index = len(self.values)
        self.values.append(value)
        self.labels.append(label)
        self.active.append(True)
        self.geom_values.append(get_geom_values)
        self.bounds.append(bounds)

        return new_index

    def get_geometric_values(self):
        """
        Evaluate the geometric values of the stored paramters.

        Returns
        -------
        list of float

        """
        return [get_geom() for get_geom in self.geom_values]

    def set_active_parameters(self, indices):
        """
        Include the designated parameters in the optimization process.

        It modifies the :py:attr:`active<OptimizationParameters.active>`
        attribute.

        Parameters
        ----------
        indices : 'all' or list of int
            If `"all"`, all the stored parameters are included, either only the
            parameters corresponding to the given indices are included.

        """
        if isinstance(indices, str) and indices == 'all':
            active = np.ones_like(self.active)
        else:
            active = np.zeros_like(self.active)
            active[indices] = True
        self.active = active.tolist()

    def get_active_values(self):
        """
        Return the value of the parameters included in the optimization process

        Returns
        -------
        optim_values : list of float

        """
        optim_values = [value for (value, optim) in
                        zip(self.values, self.active) if optim]
        return optim_values

    def get_active_bounds(self):
        """
        Return the bounds of the parameters included in the optim. process.

        Returns
        -------
        bounds : list of tuple of float

        """
        bounds = [(bound[0] + self.MARGIN, bound[1] - self.MARGIN)
                  for (bound, optim) in zip(self.bounds, self.active) if optim]
        return bounds

    def set_active_values(self, new_values):
        """
        Modify the value of the parameters included in the optim. process.

        It is typically done at each step of an optimization process.

        Parameters
        ----------
        new_values : list of float
            The list of the new values. Its length must correspond to the
            number of parameters included in the optimization process (True in
            :py:attr:`active<OptimizationParameters.active>`)

        """
        values = np.array(self.values)
        values[self.active] = new_values
        self.values = values.tolist()

    def get_param(self, param_index):
        """
        Get the value of the designated parameter

        Parameters
        ----------
        param_index : int
            The index at which is stored the desired parameter.

        Returns
        -------
        float

        """
        return self.values[param_index]

    def diff_param(self, param_index, diff_index):
        """
        Differentiate the parameter with respect to one parameter.

        .. math::
            \\frac{\\partial \\zeta_k}{\\partial \\zeta_l}

        The result is typically 1 or 0.

        Parameters
        ----------
        param_index : int
            The parameter which is differentiate (:math:`k`).
        diff_index : int
            The index of the parameter w.r. to which the differentiation is
            computed (:math:`l`).

        Returns
        -------
        dparam : float
            The value of the differentiate: 1 if the two parameters correspond
            (:math:`k=l`), 0 either.
        """
        indices_active = np.where(self.active)[0]
        if param_index == indices_active[diff_index]:
            dparam = 1.
        else:
            dparam = 0.
        return dparam



# === The Different Kinds of Parameters ===


class DesignParameter(ABC):
    """
    A geometric parameter used to design an instrument.

    It is used to parameterized a :py:class:`DesignShape<openwind.design.DesignShape>`,
    or to specify the location of a side hole on the main bore.

    Parent class of the different kinds of parameters.
    """

    @abstractmethod
    def get_value(self):
        """Current geometric value of the parameter."""

    @abstractmethod
    def set_value(self, value):
        """
        set new geometric value of the parameter.

        Parameters
        ----------
        value : float
            The new value
        """

    @abstractmethod
    def get_differential(self, diff_index):
        """
        Differentiate the parameter with respect to one optimization variable.

        Parameters
        ----------
        diff_index : int
            Index of the active parameter of the :py:class:`OptimizationParameters \
            <openwind.design.design_parameter.OptimizationParameters>`
            considered for the differentiation.

        Return
        ---------
        float
            The value of the differentiale (Typically 1 or 0).

        """

    @abstractmethod
    def is_variable(self):
        """Variable status (Fixed: False, else: True)."""

    def __str__(self):
        return "{:<7.5g}".format(self.get_value())

    def __repr__(self):
        return '{label}:{class_}({value})'.format(label=self.label,
                                                  class_=type(self).__name__,
                                                  value = self.__str__())


class FixedParameter(DesignParameter):
    """
    Parameter with a constant value.

    Parameters
    -----------
    value : float
        The geometric value of the parameter
    label : str, optional
        The parameter's name. The default is ''.

    """

    def __init__(self, value, label=''):
        self._value = value
        self.label = label

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_differential(self, diff_index):
        return 0

    def is_variable(self):
        return False


class VariableParameter(DesignParameter):
    """
    Variable geometric design parameter.

    Parameter the value of which can be possibly modify after instanciation,
    for example during an optimization process. The use of this class is
    coupled with the :py:class:`OptimizationParameters \
    <openwind.design.design_parameter.OptimizationParameters>`.

    The geometric value equals the stored optimized value. This value is
    bounded such as:

    .. math::
        x_{min}<x<x_{max}


    Parameters
    ----------
    value : float
        The initial geometric value of the parameter
    optim_params : :py:class:`OptimizationParameters \
    <openwind.design.design_parameter.OptimizationParameters>`
        The object where is stored the variable value
    label : str, optional
        The name of the parameter. the default is ''.
    bounds : list of two float
        The boundaries :math:`x_{min}` and :math:`x_{max}` of the authorized
        range for this parameter. The default is no bounds: `(-inf, inf)`

    Attributes
    ----------
    label : str
        The parameter name.
    index : int
        The position at which is stored this parmeter in the
        :py:class:`OptimizationParameters`
    """

    def __init__(self, value, optim_params, label='',
                 bounds=(-np.inf, np.inf)):
        self._optim_params = optim_params
        self.label = label
        if bounds[0] > bounds[1]:
            raise ValueError('The low bound {} must be smaller than the upper'
                             ' bound {}'.format(bounds[0], bounds[1]))
        if (value <= bounds[0] or value >= bounds[1]):
            raise ValueError('The initial value is not inside the authorized '
                             'range.')
        self.index = optim_params.new_param(value, label, self.get_value,
                                            bounds)

    def get_value(self):
        return self._optim_params.get_param(self.index)

    def set_value(self, value):
        self._optim_params.values[self.index] = value

    def get_differential(self, diff_index):
        return self._optim_params.diff_param(self.index, diff_index)

    def is_variable(self):
        return True

    def __str__(self):
        bounds = self._optim_params.bounds[self.index]
        msg = "~{:>.5g}".format(self.get_value())
        if not all(np.isinf(bounds)):
            msg = "{}<".format(bounds[0]) + msg
            if not np.isinf(bounds[1]):
                msg += "<{}".format(bounds[1])
        return msg


class VariableHolePosition(DesignParameter):
    """
    Variable hole position defined relatively on the main bore pipe.

    The location of the hole :math:`x_{hole}` is defined as:

    .. math::
        \\begin{align}
        x_{hole} & =  (x_1 - x_0) \\zeta + x_0 \\\\
        0 & \\leq \\zeta \\leq 1
        \\end{align}

    with :math:`\\zeta` an auxiliary parameter bounded between 0 and 1,
    :math:`(x_{0},x_{1})` the boundaries of the main bore pipe
    where is placed the considered hole. It's assure that:
    :math:`x_0 \\leq x_{hole} \\leq x_1`.

    .. warning::
        The stocked and optimized value is :math:`\\zeta` and not \
        :math:`x_{hole}`

    Parameters
    ----------
    init_value : float
        The initial geometric value of the parameter
    optim_params : :py:class:`OptimizationParameters \
    <openwind.design.design_parameter.OptimizationParameters>`
        The object where is stored the variable value
    main_bore_shape : :py:class:`DesignShape <openwind.design.DesignShape>`
        The shape of the pipe where is located the hole.
    label : str, optional
        The name of the parameter. the default is ''.

    Attributes
    ----------
    label : str
        The parameter name.
    index : int
        The position at which is stored this parmeter in the
        :py:class:`OptimizationParameters \
        <openwind.design.design_parameter.OptimizationParameters>`
    """

    def __init__(self, init_value, optim_params, main_bore_shape, label=''):
        self._optim_params = optim_params
        self.label = label
        self._main_bore_shape = main_bore_shape
        norm_position = main_bore_shape.get_xnorm_from_position(init_value)
        self.index = optim_params.new_param(norm_position, label,
                                            self.get_value, (0, 1))

    def is_variable(self):
        return True

    def get_value(self):
        x_norm = self._optim_params.get_param(self.index)
        value = self._main_bore_shape.get_position_from_xnorm(x_norm)
        return value

    def set_value(self, value):
        norm_position = self._main_bore_shape.get_xnorm_from_position(value)
        self._optim_params.values[self.index] = norm_position

    def get_differential(self, diff_index):
        d_zeta = self._optim_params.diff_param(self.index, diff_index)
        zeta = self._optim_params.get_param(self.index)

        x_norm = zeta
        dx_norm = d_zeta

        Xmin, Xmax = eval_(self._main_bore_shape.get_endpoints_position())
        d_position = (self._main_bore_shape
                      .get_diff_position_from_xnorm(x_norm, diff_index))
        return dx_norm*(Xmax - Xmin) + d_position

    def __str__(self):
        return "~{:>.5g}%".format(self.get_value())


class VariableHoleRadius(DesignParameter):
    """
    Variable hole radius defined relatively to the main bore pipe radius.

    The hole raidus :math:`r_{hole}` is defined as:

    .. math::
        \\begin{align}
        r_{hole} & = r_{main} \\zeta \\\\
        0 & \\leq \\zeta \\leq 1
        \\end{align}

    with :math:`\\zeta` an auxiliary parameter bounded between 0 and 1,
    :math:`r_{main}` the radius of the main bore pipe at the
    position of the considered hole. It's assure that:
    :math:`r_{hole} \\leq r_{main}`

    .. warning::
        The stocked and optimized value is :math:`\\zeta` and not \
        :math:`r_{hole}`

    Parameters
    ----------
    init_value : float
        The initial geometric value of the parameter
    optim_params : :py:class:`OptimizationParameters \
    <openwind.design.design_parameter.OptimizationParameters>`
        The object where is stored the variable value
    main_bore_shape :  :py:class:`DesignShape <openwind.design.DesignShape>`
        The shape of the pipe where is located the hole.
    hole_position : :py:class:`DesignParameter \
    <openwind.design.design_parameter.DesignParameter>`
        The position of the hole.
    label : str, optional
        The name of the parameter. the default is ''.

    Attributes
    ----------
    label : str
    index : int
        The position at which is stored this parmeter in the
        `OptimizationParameters`
    """

    def __init__(self, init_value, optim_params, main_bore_shape,
                 hole_position, label=''):
        self._optim_params = optim_params
        self.label = label
        self._hole_position = hole_position
        self._main_bore_shape = main_bore_shape

        x_norm = self.__get_x_norm()
        radius_main_pipe = main_bore_shape.get_radius_at(x_norm)
        # zeta = inv_sigmoid(init_value/radius_main_pipe)
        zeta = init_value/radius_main_pipe
        self.index = optim_params.new_param(zeta, label, self.get_value,
                                            (0, 1))

    def is_variable(self):
        return True

    def get_value(self):
        zeta = self._optim_params.get_param(self.index)
        x_norm = self.__get_x_norm()
        radius_main_pipe = self._main_bore_shape.get_radius_at(x_norm)
        value = radius_main_pipe * zeta
        return value

    def set_value(self, value):
        x_norm = self.__get_x_norm()
        radius_main_pipe = self._main_bore_shape.get_radius_at(x_norm)
        zeta = value/radius_main_pipe
        self._optim_params.values[self.index] = zeta

    def __get_x_norm(self):
        pos = self._hole_position.get_value()
        return self._main_bore_shape.get_xnorm_from_position(pos)

    def __get_diff_x_norm(self, diff_index):
        dXmin, dXmax = diff_(self._main_bore_shape.get_endpoints_position(),
                             diff_index)
        Xmin, Xmax = eval_(self._main_bore_shape.get_endpoints_position())
        dPos = self._hole_position.get_differential(diff_index)
        Pos = self._hole_position.get_value()
        return (((dPos - dXmin)*(Xmax - Xmin) - (Pos - Xmin)*(dXmax - dXmin))
                / (Xmax - Xmin)**2)

    def get_differential(self, diff_index):
        d_zeta = self._optim_params.diff_param(self.index, diff_index)
        zeta = self._optim_params.get_param(self.index)

        x_norm = self.__get_x_norm()
        r_pipe = self._main_bore_shape.get_radius_at(x_norm)

        dx_norm = self.__get_diff_x_norm(diff_index)
        dr_pipe_dx_norm = self._main_bore_shape.diff_radius_wr_x_norm(x_norm)
        dr_pipe_diff_index = (self._main_bore_shape
                              .get_diff_radius_at(x_norm, diff_index))
        return (d_zeta*r_pipe
                + zeta*dr_pipe_dx_norm*dx_norm
                + zeta*dr_pipe_diff_index)

    def __str__(self):
        return "~{:>.5g}%".format(self.get_value())
