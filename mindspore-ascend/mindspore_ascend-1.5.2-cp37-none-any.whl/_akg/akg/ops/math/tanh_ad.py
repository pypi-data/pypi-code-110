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

"""operator dsl function: tanh_ad"""
import akg.tvm
import akg.topi
import akg
from akg.ops.math import tanh
from akg.utils import kernel_exec as utils
from akg.utils import validation_check as vc_util


@vc_util.check_input_type(akg.tvm.tensor.Tensor, akg.tvm.tensor.Tensor)
def tanh_ad(head, in_data):
    """
    Compute gradient of tanh operator using automatic differentiate.

    Args:
        head (tvm.tensor.Tensor): Tensor of type float16, float32.
        in_data (tvm.tensor.Tensor): Tensor of type float16, float32.

    Returns:
        tvm.tensor.Tensor has the same shape as input.
    """
    in_dtype = in_data.dtype

    # On cloud environment, cast data type from 'float16' to 'float32',
    # then cast result back to 'float16', could achieve higher precision.
    if in_dtype == 'float16' and not utils.product_is_mini():
        in_data = akg.topi.cast(in_data, "float32")
        head = akg.topi.cast(head, "float32")

    out_data = tanh.tanh(in_data)
    jacs = list(akg.differentiate(out_data, [in_data], head))
    jacs_res = jacs[0]
    if in_dtype == 'float16' and not utils.product_is_mini():
        jacs_res = akg.topi.cast(jacs_res, 'float16')
    return jacs_res
