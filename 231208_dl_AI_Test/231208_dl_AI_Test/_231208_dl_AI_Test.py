
# 텐서 플로우 로드


import _01_Prologue
import _02_Data
import _03_TextGenerate

import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# import tensorflow as tf
# from tensorflow.python.client import device_lib
# device_lib.list_local_devices()


# tf.debugging.set_log_device_placement(True)


#_01_Prologue.TestPrologue();
#_02_Data.DataSetTest();
_02_Data.ModelTestUser();
#_03_TextGenerate.TextGenarateTest()
