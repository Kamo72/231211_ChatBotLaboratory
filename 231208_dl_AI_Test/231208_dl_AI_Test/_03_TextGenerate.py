import tensorflow as tf
import numpy as np

def TextGenarateTest ():
    # �Ʒ� ������ �غ�
    data = ["Hello", "World", "ChatGPT", "TensorFlow", "Model", "String", "Input", "Output"]

    # �Է� ������ ����
    input_sequences = [text.lower() for text in data]
    output_sequences = [text[::-1] for text in input_sequences]  # ������ ������ ���÷� ���

    # ��ūȭ
    tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)
    tokenizer.fit_on_texts(input_sequences)

    # �Ʒ� �����͸� ���� �������� ��ȯ
    input_sequences_numeric = tokenizer.texts_to_sequences(input_sequences)
    output_sequences_numeric = tokenizer.texts_to_sequences(output_sequences)

    # �е�
    input_sequences_padded = tf.keras.preprocessing.sequence.pad_sequences(input_sequences_numeric)
    output_sequences_padded = tf.keras.preprocessing.sequence.pad_sequences(output_sequences_numeric)

    # �� ����
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=16, input_length=input_sequences_padded.shape[1]),
        tf.keras.layers.LSTM(32),
        tf.keras.layers.Dense(len(tokenizer.word_index) + 1, activation='softmax')
    ])

    # �� ������
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # ���̺� ������ ��ȯ
    output_sequences_padded_numeric = tf.keras.preprocessing.sequence.pad_sequences(output_sequences_numeric, padding='post')

    # �� �Ʒ�
    model.fit(input_sequences_padded, output_sequences_padded_numeric, epochs=50)

    # ���� �Լ� ����
    def generate_text(model, seed_text, tokenizer, max_length):
        for _ in range(max_length):
            # ���� �ؽ�Ʈ�� ��ūȭ
            input_seq = tokenizer.texts_to_sequences([seed_text])[0]
            # �е�
            input_seq = tf.keras.preprocessing.sequence.pad_sequences([input_seq], maxlen=input_sequences_padded.shape[1])
            # �� ����
            predicted_token = model.predict_classes(input_seq, verbose=0)
            # ��ū�� �ܾ�� ��ȯ
            predicted_text = tokenizer.index_word[predicted_token[0]]
            # ���� �ؽ�Ʈ�� �߰�
            seed_text += predicted_text
        return seed_text

    # �׽�Ʈ
    seed_text = "hello"
    generated_text = generate_text(model, seed_text, tokenizer, max_length=5)
    print(f"Input: {seed_text}, Generated Output: {generated_text}")