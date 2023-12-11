import tensorflow as tf
import numpy as np

def TextGenarateTest ():
    # 훈련 데이터 준비
    data = ["Hello", "World", "ChatGPT", "TensorFlow", "Model", "String", "Input", "Output"]

    # 입력 시퀀스 생성
    input_sequences = [text.lower() for text in data]
    output_sequences = [text[::-1] for text in input_sequences]  # 간단한 반전을 예시로 사용

    # 토큰화
    tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)
    tokenizer.fit_on_texts(input_sequences)

    # 훈련 데이터를 숫자 시퀀스로 변환
    input_sequences_numeric = tokenizer.texts_to_sequences(input_sequences)
    output_sequences_numeric = tokenizer.texts_to_sequences(output_sequences)

    # 패딩
    input_sequences_padded = tf.keras.preprocessing.sequence.pad_sequences(input_sequences_numeric)
    output_sequences_padded = tf.keras.preprocessing.sequence.pad_sequences(output_sequences_numeric)

    # 모델 정의
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=16, input_length=input_sequences_padded.shape[1]),
        tf.keras.layers.LSTM(32),
        tf.keras.layers.Dense(len(tokenizer.word_index) + 1, activation='softmax')
    ])

    # 모델 컴파일
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # 레이블 데이터 변환
    output_sequences_padded_numeric = tf.keras.preprocessing.sequence.pad_sequences(output_sequences_numeric, padding='post')

    # 모델 훈련
    model.fit(input_sequences_padded, output_sequences_padded_numeric, epochs=50)

    # 예측 함수 정의
    def generate_text(model, seed_text, tokenizer, max_length):
        for _ in range(max_length):
            # 현재 텍스트를 토큰화
            input_seq = tokenizer.texts_to_sequences([seed_text])[0]
            # 패딩
            input_seq = tf.keras.preprocessing.sequence.pad_sequences([input_seq], maxlen=input_sequences_padded.shape[1])
            # 모델 예측
            predicted_token = model.predict_classes(input_seq, verbose=0)
            # 토큰을 단어로 변환
            predicted_text = tokenizer.index_word[predicted_token[0]]
            # 현재 텍스트에 추가
            seed_text += predicted_text
        return seed_text

    # 테스트
    seed_text = "hello"
    generated_text = generate_text(model, seed_text, tokenizer, max_length=5)
    print(f"Input: {seed_text}, Generated Output: {generated_text}")