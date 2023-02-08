import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import pyautogui
import time
import pyautogui
import mysql.connector


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """This function is use to speak by the pc"""
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """This is use to wish when you open the voice assistant"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<16:
        speak('good afternoon')
        
    else:
        speak('good evening')
    speak('I am jarvis, how I can Help You?')

def take_command():
    """ This is use to take command from the user"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listining...')
        r.energy_threshold=1000
        print("1")
        audio=r.listen(source)
        print("2")
    try:
        print('recognising...')
        query=r.recognize_google(audio,language='en-in')
        print('User Said:',query)
        time.sleep(1)
    except Exception as e :
        #print(e)
        speak('i can not understand, please ,say that again')
        
        print('say again..')
        return 'None'
    return query

def exit():
    

    """This is use to exist the pogram"""
    speak('bye, see you again')
    quit() 


def play():
    """This contain all condition for voice assistant"""
    while True:
        query= take_command().lower()
        print(query)

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('on wikipedia','')
            query=query.replace('search','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')


        elif 'open vs code' in query:
            speak('opening vs code')
            codepath=r'"C:\Users\Devsa\AppData\Local\Programs\Microsoft VS Code\Code.exe"'
            os.startfile(codepath)

        elif 'exit' in query:
            break
    
        input('press enter to continue')

    
wishme()
play()
