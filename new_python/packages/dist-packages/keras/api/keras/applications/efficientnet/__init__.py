# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""EfficientNet models for Keras.

Reference:
  - [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](
      https://arxiv.org/abs/1905.11946) (ICML 2019)

"""

import sys as _sys

from keras.applications.efficientnet import EfficientNetB0
from keras.applications.efficientnet import EfficientNetB1
from keras.applications.efficientnet import EfficientNetB2
from keras.applications.efficientnet import EfficientNetB3
from keras.applications.efficientnet import EfficientNetB4
from keras.applications.efficientnet import EfficientNetB5
from keras.applications.efficientnet import EfficientNetB6
from keras.applications.efficientnet import EfficientNetB7
from keras.applications.efficientnet import decode_predictions
from keras.applications.efficientnet import preprocess_input
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.applications.efficientnet", public_apis=None, deprecation=True,
      has_lite=False)