# Copyright 2020 Google Research. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""A tool for model optimization."""
import functools

import tensorflow_model_optimization as tfmot
from tensorflow_model_optimization.python.core.quantization.keras import quantize_wrapper
from tensorflow_model_optimization.python.core.quantization.keras.default_8bit import default_8bit_quantize_configs


def quantize(layer, quantize_config=None):
  if quantize_config is None:
    quantize_config = default_8bit_quantize_configs.Default8BitOutputQuantizeConfig(
    )
  return quantize_wrapper.QuantizeWrapper(
      layer, quantize_config=quantize_config)


optimzation_methods = {
    'prune': tfmot.sparsity.keras.prune_low_magnitude,
    'quantize': quantize
}


def set_config(configs):
  for key in configs:
    if key == 'prune':
      optimzation_methods[key] = functools.partial(
          tfmot.sparsity.keras.prune_low_magnitude, **configs[key])
    if key == 'quantize':
      optimzation_methods[key] = functools.partial(quantize, **configs[key])


def get_method(method):
  if method not in optimzation_methods:
    raise KeyError(f'only support {optimzation_methods.keys()}')
  return optimzation_methods[method]
