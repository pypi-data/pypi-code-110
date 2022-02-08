#!/usr/bin/env python3
# coding: utf-8
# Copyright 2020 Huawei Technologies Co., Ltd
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

"""batchmatmul"""
from akg.ops.nn import matmul

def BatchMatMul(x1, x2, transpose_a=False, transpose_b=False):
    """use cube version matmul"""
    return matmul.matmul(x=x1, y=x2, b=None, out_dtype=x1.dtype,
                         left_format="zN", right_format="zN", out_format="zN",
                         transpose_x=transpose_a, transpose_y=transpose_b)
