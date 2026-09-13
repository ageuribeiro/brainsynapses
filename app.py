import speech_recognition as sr
import pyttsx3
import os

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_tensorflow(audio)
            text = text.__str__()
            print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

        recognizer = sr.Recognizer()
        continue
