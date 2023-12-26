# -*- coding: cp949 -*-
import io
import os

# API 키가 필요함. 같이 포함된 파일인
# dotted-hope-405202-5a8098f32014.json
# 를 GOOGLE_APPLICATION_CREDENTIALS 환경 변수로 지정해줘야 함
from google.cloud import speech
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


print(sd.query_devices())


def record_and_save(filename, duration=5, samplerate=16000):
    # 음성 녹음
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    # recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16, device=8)
    # 녹음 장치에 문제 있으면 위의 코드로 교체
    sd.wait()
    
    # WAV 파일로 저장
    wav.write(filename, samplerate, recording)

# Instantiates a client
client = speech.SpeechClient()


print(f"녹음이 시작됩니다. {5}초 동안 대기하세요...")
record_and_save("recorded_audio.wav")
print(f"녹음이 완료되었습니다. 파일: recorded_audio.wav")

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'recorded_audio.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='ko-KR')

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

a = input()
exit()


