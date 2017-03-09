#/etc/bin/env python3
import time
import aiml
import os
import time
def botsay(str,end="\n"):
    print("Bucky :>"str,end="\n")

def readin():
    return input()

def get_aiml():
    #for folder in os.listdir():
    return
        
def set_alarm(timevar):
    """
    Sets an alarm
    """
    
    return
    
def mainfunc():
    botsay("Hello I am Bucky, Your personal asistant...")
    while True:
        print("You :>")
        inp = readin()
        if inp == "what is the time now":
            botsay("The time is " + time.strftime("%I:%M %p"))
            
        else:
            botsay("Unknown command....")
if __name__ == "__main__":
    