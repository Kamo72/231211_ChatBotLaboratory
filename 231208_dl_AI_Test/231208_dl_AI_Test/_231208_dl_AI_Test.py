
# 텐서 플로우 로드


import _01_Prologue
import _02_Data

import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print("-----------device_lib------------")
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

print("-----------device_lib------------")

# tf.debugging.set_log_device_placement(True)


#_01_Prologue.TestPrologue();
#_02_Data.DataSetTest();
_02_Data.ModelTestUser();

