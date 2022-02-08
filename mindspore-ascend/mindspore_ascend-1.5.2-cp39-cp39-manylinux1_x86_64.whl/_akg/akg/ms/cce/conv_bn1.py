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

"""ConvBN1 operator register"""
from akg.ops.nn import conv_bn1

def ConvBN1(x, x_shape, w, w_shape, pad_list, stride=1, dilation=1):
    """ConvBN1"""

    if len(pad_list) != 4:
        raise IndexError("Length of pad must be equal 4")
    pad = pad_list

    data = []
    data.append(x)
    data.append(w)
    fmap_shape = x_shape   # 4D
    filter_shape = w_shape  # 4D
    stride = [stride, stride]
    dilation = [dilation, dilation]
    return conv_bn1.conv_bn1(data, fmap_shape, filter_shape,
                             pad, stride, dilation,
                             use_bias=False, attrs=None)
