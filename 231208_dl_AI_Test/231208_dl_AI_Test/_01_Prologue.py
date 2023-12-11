
# �ټ� �÷ο� �ε�
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

    # Sequential�� �� ���̾ �ϳ��� �Է� �ټ��� �ϳ��� ��� �ټ��� �ִ� ���̾ �״� �� �����մϴ�.
    # ���̾�� ������ �����ϰ� �Ʒ� ������ ������ ���� �˷��� ������ ������ ���� �Լ��Դϴ�.
    # ��κ��� TensorFlow ���� ���̾�� �����˴ϴ�. �� ���� Flatten, Dense �� Dropout ���̾ ����մϴ�.
    # �� ���� ���� ���� �� Ŭ������ ���� �ϳ��� ����Ʈ �Ǵ� �α� Ȯ�� ������ ���͸� ��ȯ�մϴ�.
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



