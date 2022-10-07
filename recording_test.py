import speech_recognition as sr
import sys

# 함수 정의부
def get_speech():
    # 마이크에서 음성을 추출하는 객체
    recognizer = sr.Recognizer()

    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"소음 수치를 반영하여 음성을 청취합니다. {recognizer.energy_threshold}")

    # 음성 수집
    with microphone as source:
        print("오늘 어때요??")
        speech = recognizer.listen(source)
        # audio = result.get_raw_data()
        try:
            audio = recognizer.recognize_google(speech, language="ko-KR")
            print(f"Your speech thinks like\n{audio}")
        except sr.UnknownValueError:
            print("Your speech can not understand")
        except sr.RequestError as e:
            print(f"Request Error!! {e}")

if __name__ == "__main__":
    get_speech()
