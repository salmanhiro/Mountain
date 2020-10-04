import speech_recognition as sr
import os
from gtts import gTTS

def recordAudio():    
    # Record the audio
    r = sr.Recognizer()
    with sr.Microphone() as source:  
       print('Say something!')
       audio = r.listen(source)
    
    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')
    return data