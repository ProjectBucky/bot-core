#/etc/bin/env python2
import time
import aiml
from aiml import Kernel
from os import listdir
import sys

files = listdir('aiml')
bot = Kernel()
for file in files:
    bot.learn('aiml/'+file)

def botsay(str,end="\n"):
    print("Bucky :>"+str)

def readin(msg):
    tempx = str(raw_input(msg))
    return tempx
        
def set_alarm(timevar):
    """
    Sgets an alarm
    """
    return
    
def mainfunc():
    botsay("Hello I am Bucky, Your personal asistant...")
    while True:
        inp = readin("You> ")
        if inp == "what is the time now":
            botsay("The time is " + time.strftime("%I:%M %p"))
            
        else:
            ans = bot.respond(inp)
            botsay(ans)

if __name__ == "__main__":
    mainfunc()
