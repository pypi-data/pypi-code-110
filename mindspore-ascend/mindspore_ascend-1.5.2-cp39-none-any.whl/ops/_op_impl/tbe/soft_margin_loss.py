# Copyright 2021 Huawei Technologies Co., Ltd
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

"""SoftMarginLoss op"""
from mindspore.ops.op_info_register import op_info_register, TBERegOp, DataType

soft_margin_loss_op_info = TBERegOp("SoftMarginLoss") \
    .fusion_type("OPAQUE") \
    .async_flag(False) \
    .binfile_name("soft_margin_loss.so") \
    .compute_cost(10) \
    .kernel_name("soft_margin_loss") \
    .partial_flag(True) \
    .attr("reduction", "optional", "str", "mean,none,sum", "mean") \
    .input(0, "input_x", False, "required", "all") \
    .input(1, "input_y", False, "required", "all") \
    .output(0, "output_z", False, "required", "all") \
    .dtype_format(DataType.F32_Default, DataType.F32_Default, DataType.F32_Default) \
    .dtype_format(DataType.F16_Default, DataType.F16_Default, DataType.F16_Default) \
    .get_op_info()


@op_info_register(soft_margin_loss_op_info)
def _soft_margin_loss_tbe():
    """SoftMarginLoss TBE register"""
    return
