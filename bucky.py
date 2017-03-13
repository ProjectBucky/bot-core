#/etc/bin/env python2
import time
import aiml
import os
from aiml import Kernel
from os import listdir
import speech_recognition as sr
import sys
import pyttsx

r = sr.Recognizer()
files = listdir('aiml')
bot = Kernel()
for file in files:
    bot.learn('aiml/'+file)


def botsay(str,end="\n"):
    print("Bucky :> "+str)
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def readin():
    #tempx = str(raw_input(msg))
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        res = r.recognize_google(audio)
        print("You > "+res)
        return res
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand you...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
def readinkey():
    return str(raw_input("You > "))

def set_alarm(timevar):
    """
    Sgets an alarm
    """
    return
    
def mainfunc():
    botsay("Hello I am Bucky, Your personal asistant...")
    while True:
        inp = readinkey()
        if inp == "what is the time now":
            botsay("The time is " + time.strftime("%I:%M %p"))
        elif inp == "bye":
            ans = bot.respond(inp)
            botsay(ans)
            exit(0)   
        else:
            ans = bot.respond(inp)
            botsay(ans)


if __name__ == "__main__":
    mainfunc()
