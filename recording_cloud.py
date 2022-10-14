import pyaudio
import wave
import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

# send_kakaotalk.py를 import한 뒤, 음성 번역한 값을 do()의 인수로 넘겨준다.
import send_kakaotalk

def recording():
    # 녹음파일의 설정을 정하는 과정이다.
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    # 목소리 녹음 시작
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print("오늘 어때요??")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): # 약 5초간 음성을 인식한다.
        data = stream.read(CHUNK)
        frames.append(data)
    print ("아하! 그렇군요!")

    # 목소리 녹음 종료
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    run_quickstart() # run_quickstart()는 음성파일을 Google의 서비스가 듣고 텍스트로 번역한다.

def run_quickstart():
    client = speech.SpeechClient()

    file_name = os.path.join(os.path.dirname(__file__), ".", "file.wav")


    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000, # sampling rate는 16000이다.
        language_code="ko-KR", # ko-KR로 해야 음성이 한국말인 것을 인지하고 번역한다.
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"이렇게 말씀하신거 맞죠?\n{result.alternatives[0].transcript}")
        send_kakaotalk.do(result.alternatives[0].transcript) # send_kakatalk의 do()에게 번역된 텍스트를 주었다.


if __name__ == "__main__":
    recording()