# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Keras mixed precision API.

See [the mixed precision guide](
  https://www.tensorflow.org/guide/keras/mixed_precision) to learn how to
use the API.

"""

import sys as _sys

from keras.mixed_precision.loss_scale_optimizer import BaseLossScaleOptimizer as LossScaleOptimizer
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.mixed_precision", public_apis=None, deprecation=True,
      has_lite=False)