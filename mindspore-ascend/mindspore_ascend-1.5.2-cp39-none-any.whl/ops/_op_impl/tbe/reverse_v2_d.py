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
# ============================================================================

"""ReverseV2D op"""
from mindspore.ops.op_info_register import op_info_register, TBERegOp, DataType

reverse_v2_d_op_info = TBERegOp("ReverseV2") \
    .fusion_type("ELEMWISE") \
    .async_flag(False) \
    .binfile_name("reverse_v2_d.so") \
    .compute_cost(10) \
    .kernel_name("reverse_v2_d") \
    .partial_flag(True) \
    .is_dynamic_format(True) \
    .attr("axis", "required", "listInt", "all") \
    .input(0, "x", False, "required", "all") \
    .output(0, "y", False, "required", "all") \
    .dtype_format(DataType.None_None, DataType.None_None) \
    .get_op_info()


@op_info_register(reverse_v2_d_op_info)
def _reverse_v2_d_tbe():
    """ReverseV2D TBE register"""
    return
