import pyaudio
import wave
import io
import os
# Imports the Google Cloud client library
from google.cloud import speech

import send_kakaotalk

def recording():
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

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")

# stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    run_quickstart()

def run_quickstart():
    client = speech.SpeechClient()

    file_name = os.path.join(os.path.dirname(__file__), ".", "file.wav")


    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript : {result.alternatives[0].transcript}")
        send_kakaotalk.do(result.alternatives[0].transcript)


if __name__ == "__main__":
    recording()