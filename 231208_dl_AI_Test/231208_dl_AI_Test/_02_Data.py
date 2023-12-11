
# �ټ� �÷ο� �ε�
from asyncio.windows_events import NULL
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.gen_control_flow_ops import switch
print("TensorFlow version:", tf.__version__)


#tf.data.Dataset

def DataSetPrintItem(dataset) :
    print("DataSetPrint : ", end=" ")
    for item in dataset:
        print(item.numpy(), end=" ")
    print("")
    
def DataSetPrintBatch(dataset) :
    print("DataSetPrint : ", end=" ")
    for batch in dataset:
        print(batch.numpy())
    print("")
    
@tf.autograph.experimental.do_not_convert
def DataSetTest ():
    #array >> dataSet
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
    DataSetPrintItem(dataset)
    
    #map
    dataset = dataset.map(lambda x: x * 2)
    DataSetPrintItem(dataset)
    
    #filter
    dataset = dataset.filter(lambda x: x > 2)
    DataSetPrintItem(dataset)

    #repeat
    dataset = dataset.repeat(3)
    DataSetPrintItem(dataset)
    
    #shuffle
    dataset = dataset.shuffle(buffer_size=100)
    DataSetPrintItem(dataset)

    #batch
    dataset = dataset.batch(batch_size=3)
    DataSetPrintBatch(dataset)

def ModelTest ():
    # �� ����
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1)  # ���� ���̾� (��� ���� Ȱ��ȭ �Լ��� ��ġ�� ����)
    ])

    # �� ������
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    
    # �Ʒ� ������ ����
    X_train = np.arange(0, 100, 1).reshape(-1, 1)
    y_train = X_train * X_train

    # �� �Ʒ�
    model.fit(X_train, y_train, epochs=1000)
    
    # �׽�Ʈ ������ ����
    X_test = np.array([[5], [10], [15], [215], [-23], [0], [1], [2], [9241]])  # ���÷� 5, 10, 15�� �Է��غ��ڽ��ϴ�.

    # �� ����
    predictions = model.predict(X_test)

    # ��� ���
    print("Math.Pow() AI")
    for i in range(len(X_test)):
        print(f"Input: {X_test[i][0]}, Predicted Output: {predictions[i][0]}")
    
def ModelTestUser ():
    
    model = NULL;
    user_input = ""
    
    while(True) :
        user_input = input("insert number(insert '/' to Exit , 'm' to More Learning, 's' to Save, 'l' to Load) : ")
        try:
            float_value = float(user_input)
            predictionsInput = model.predict(np.array([[float_value]]))
            print(f"Predicted Output: {predictionsInput[0][0]}")
        except ValueError:
            match user_input :
                case "/" :
                    break
                case "m" :
                    if (model == NULL) : 
                        print("model not Loaded!")
                        continue
                    
                    model = ModelTestUserMoreLearn(model)
                    
                case "s" :
                    if (model == NULL) :
                        print("model not Loaded!")
                        continue
                    
                    model.save("my_model.keras");
                
                case "l" :
                    try :
                        model = tf.keras.models.load_model("my_model.keras")
                        # �� ������
                        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
                        print("Model Load Complete! ")
                    except (OSError, IOError) as e:
                        print("model not Loaded! I'll Create it now...")
                        model = tf.keras.Sequential([
                            tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
                            tf.keras.layers.Dense(1)  # ���� ���̾� (��� ���� Ȱ��ȭ �Լ��� ��ġ�� ����)
                        ])
                        # �� ������
                        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
                        print("Model Create Complete! ")
                case _:
                    print("not Valid user input.")

def ModelTestUserMoreLearn(model) :
     # �Ʒ� ������ ����
    X_train = np.arange(0, 100, 1).reshape(-1, 1)
    y_train = X_train * X_train

    # �� �Ʒ�
    model.fit(X_train, y_train, epochs=1000)
    
    # �׽�Ʈ ������ ����
    X_test = np.array([[5], [10], [15], [215], [-23], [0], [1], [2], [9241]])  # ���÷� 5, 10, 15�� �Է��غ��ڽ��ϴ�.

    # �� ����
    predictions = model.predict(X_test)

    # ��� ���
    print("Math.Pow() AI")
    for i in range(len(X_test)):
        print(f"Input: {X_test[i][0]}, Predicted Output: {predictions[i][0]}")
    
    return model
        








