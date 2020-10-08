import pyttsx3  # text to speak
import speech_recognition as sr  # use for Recognising voice
# this project require package called pyaudio which will give error on direct installing through pip.u have to write #command pip install pipwin then pip install pyaudio

import time


def listen():
    r = sr.Recognizer()
    with sr.AudioFile('7.wav') as source:
        print("speak")
        # r.speak() use to catch only first nonstop sentence
        audio = r.record(source, duration=15, offset=30)
        time.sleep(1)
        print("done")
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except Exception as e:
        print(e)


def Speak(text):
    pyttsx3.speak(text)


text = listen()

Speak(text)
