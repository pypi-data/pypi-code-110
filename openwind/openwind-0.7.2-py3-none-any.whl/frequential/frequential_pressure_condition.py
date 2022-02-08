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

"""Dirichlet boundary condition on pressure."""

import scipy.sparse

from openwind.frequential import FrequentialComponent


class FrequentialPressureCondition(FrequentialComponent):
    """
    Impose the pression at the opening (for ex. p=0, for a perfect opening)

    Dirichlet boundary condition on the pressure unknown.
    Assuming convention 'PH1', pressure is imposed through a Lagrange
    multiplier.

    The contribution of this component to the matrices :math:`A_h` and
    :math:`L_h` are:

    .. code-block::

                         ┌               ┐
                         │ .  .  .  .  . │
                         │ .  .  .  .  . │
            Ah_contrib = │ .  .  .  1  . │ ← line of the pipe end's d.o.f.
                         │ .  . -1  .  . │ ← line of this component's d.o.f.
                         │ .  .  .  .  . │
                         └               ┘

                         ┌   ┐
                         │ . │
                         │ . │
            Lh_contrib = │ . │
                         │-v │ ← line of this component's d.o.f.
                         │ . │
                         └   ┘


    with `v` the imposed value

    See Also
    --------
    :py:class:`RadiationPerfectlyOpen<openwind.continuous.physical_radiation.RadiationPerfectlyOpen>`
        The continuous version of this radiation condition.

    Parameters
    ----------
    value: float
        Pressure value imposed at the given end.

    freq_ends : :py:class:`FPipeEnd <openwind.frequential.frequential_pipe_fem.FPipeEnd>`\
        or :py:class:`TMMPipeEnd <openwind.frequential.frequential_pipe_tmm.TMMPipeEnd>`
        Pipe end associated to this radiation condition.
    """

    def __init__(self, value, freq_ends):
        self.freq_end, = freq_ends  # Unpack one
        self.value = value

    # --------------------------------------------
    # Methods overridden from FrequentialComponent
    # --------------------------------------------

    def get_number_dof(self):
        """
        Number of degrees of freedom added by this component.

        Pressure condition adds 1 Lagrange multiplier corresponding to the
        exiting flow.

        Returns
        -------
        1
        """
        return 1

    def get_contrib_indep_freq(self):
        """
        Contribution of this component to the frequency-independent terms of Ah.

        .. code-block::

                         ┌               ┐
                         │ .  .  .  .  . │
                         │ .  .  .  .  . │
            Ah_contrib = │ .  .  .  1  . │ ← line of the pipe end's d.o.f.
                         │ .  . -1  .  . │ ← line of this component's d.o.f.
                         │ .  .  .  .  . │
                         └               ┘


        Returns
        -------
        sparse matrix of size (ntot_dof x ntot_dof)

        """
        shape = (self.ntot_dof, self.ntot_dof)
        data = [1, -1]
        i = [self.freq_end.get_index(), self.get_first_index()]
        j = i[::-1]
        Ah_contrib = scipy.sparse.coo_matrix((data,(i,j)), shape)
        return Ah_contrib


    def get_contrib_freq(self, omegas_scaled):
        """
        Contribution of this component to the frequency-dependent diagonal of Ah.

        There is nothing on the diagonal.

        Parameters
        ----------
        omegas_scaled : array of float
            angular frequncies scaled thanks to :py:class:`Scaling\
            <openwind.continuous.scaling.Scaling>`

        Returns
        -------
        0

        """
        return 0

    def get_contrib_source(self):
        """
        Contribution of this component to the right-hand side Lh.

        .. code::

                         ┌   ┐
                         │ . │
                         │ . │
            Lh_contrib = │ . │
                         │-v │ ← line of this component's d.o.f.
                         │ . │
                         └   ┘

        with `v` the imposed value

        Returns
        -------
        sparse matrix with a shape ((number of dof) x 1).

        """
        shape = (self.ntot_dof, 1)
        data = [-self.value]
        i = [self.get_first_index()]
        j = [0]
        Lh_contrib = scipy.sparse.coo_matrix((data,(i,j)), shape)
        return Lh_contrib

    def get_contrib_dAh_freq(self, omegas_scaled, diff_index):
        return 0

    def get_contrib_dAh_indep_freq(self, diff_index):
        return 0
