
# 텐서 플로우 로드
from os import read
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

def TestPrologue() :
    # Load a dataset
    # Load and prepare the MNIST dataset. The pixel values of the images range from 0 through 255. Scale these values to a range of 0 to 1 by dividing the values by 255.0.
    # This also converts the sample data from integers to floating-point numbers:
    mnist = tf.keras.datasets.mnist

    # byte > 0~1f
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0


    # Build a machine learning model
    # tf.keras.Sequential model
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])

    # Sequential은 각 레이어에 하나의 입력 텐서와 하나의 출력 텐서가 있는 레이어를 쌓는 데 유용합니다.
    # 레이어는 재사용이 가능하고 훈련 가능한 변수를 갖는 알려진 수학적 구조를 가진 함수입니다.
    # 대부분의 TensorFlow 모델은 레이어로 구성됩니다. 이 모델은 Flatten, Dense 및 Dropout 레이어를 사용합니다.
    # 각 예에 대해 모델은 각 클래스에 대해 하나씩 로지트 또는 로그 확률 점수의 벡터를 반환합니다.
    predictions = model(x_train[:1]).numpy()
    predictions


    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    loss_fn(y_train[:1], predictions).numpy()

    model.compile(optimizer='adam',
                  loss=loss_fn,
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    model.evaluate(x_test,  y_test, verbose=2)

    probability_model = tf.keras.Sequential([
      model,
      tf.keras.layers.Softmax()
    ])

    probability_model(x_test[:5])



