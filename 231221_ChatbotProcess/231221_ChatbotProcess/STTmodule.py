# -*- coding: cp949 -*-
import io
import os

# API Ű�� �ʿ���. ���� ���Ե� ������
# dotted-hope-405202-5a8098f32014.json
# �� GOOGLE_APPLICATION_CREDENTIALS ȯ�� ������ ��������� ��
from google.cloud import speech
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


print(sd.query_devices())


def record_and_save(filename, duration=5, samplerate=16000):
    # ���� ����
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    # recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16, device=8)
    # ���� ��ġ�� ���� ������ ���� �ڵ�� ��ü
    sd.wait()
    
    # WAV ���Ϸ� ����
    wav.write(filename, samplerate, recording)

# Instantiates a client
client = speech.SpeechClient()


print(f"������ ���۵˴ϴ�. {5}�� ���� ����ϼ���...")
record_and_save("recorded_audio.wav")
print(f"������ �Ϸ�Ǿ����ϴ�. ����: recorded_audio.wav")

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


