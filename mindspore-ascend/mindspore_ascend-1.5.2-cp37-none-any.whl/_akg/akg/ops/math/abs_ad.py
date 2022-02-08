#!/usr/bin/env python3
# coding: utf-8
# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""operator dsl function: abs_ad"""

import akg
from akg.ops.math import abs
from akg.utils import validation_check as vc_util


@vc_util.check_input_type(akg.tvm.tensor.Tensor, akg.tvm.tensor.Tensor)
def abs_ad(head, in_data):
    """
    Compute gradient of abs operator with automatic differentiate.

    Args:
        head (tvm.tensor.Tensor): Tensor of type float16, float32, int8, uint8, int32.
        in_data (tvm.tensor.Tensor): Tensor of type float16, float32, int8, uint8, int32.

    Returns:
        tvm.tensor.Tensor has the same shape as input.
    """

    dtype = in_data.dtype
    # check head's validation.
    vc_util.check_shape(head.shape)
    vc_util.ops_dtype_check(head.dtype, vc_util.DtypeForDavinci.ALL_TYPES)
    need_cast_dtype = ["int8", "int32", "uint8"]

    abs_data = abs.abs_value(in_data)
    if head.dtype in need_cast_dtype:
        head = akg.tvm.compute(head.shape, lambda *indice: head(*indice).astype("float16"), name='head_cast')
    if dtype in need_cast_dtype:
        abs_data = akg.tvm.compute(abs_data.shape,
                                   lambda *indice: abs_data(*indice).astype("float16"),
                                   name='abs_cast')
    jacs = list(akg.differentiate(abs_data, [in_data], head))
    if dtype in need_cast_dtype:
        jacs[0] = akg.tvm.compute(jacs[0].shape, lambda *indice: jacs[0](*indice).astype(dtype), name='res')
    return jacs[0]
