# thanks for the reference at 
# https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests

backend = pyttsx3.init('nsss')
voices = backend.getProperty('voices')
backend.setProperty('voice','voices[0].id')

def speak(text):
    backend.say(text)
    backend.runAndWait()

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Time to hurry")
    elif hour >= 12 and hour < 18:
        speak("Doing your work")
    else:
        speak("Get chill")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listen........")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio,language='en')
            print(f"You said, {statement}\n")

        except Exception as e:
            speak("Could you say again?")
            return "None"
        return statement

speak("Hello! I am Mountain, your personal assistant")
greeting()

if __name__ == '__main__':
    while True:
        #os.system('open -a Terminal .')
        