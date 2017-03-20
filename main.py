import speech_recognition as sr
import pyttsx
import time
import wolframalpha
'''
engine = pyttsx.init()
engine.say("Your Message")
engine.runAndWait()
'''
def voice (str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def reply(str):
    if (str=="what is the time"):
        voice(time.strftime('%X %x %Z'))
    if (str=="what time is it"):
        voice(time.strftime('%X %x %Z'))
    if (str=="tell me the time"):
        voice(time.strftime('%X %x %Z'))
    if (str=="who are you"):
        voice("I am Bucky, the new age personal assitant")
    if (str=="what is your name"):
        voice("I am Bucky, the new age personal assitant")
    if (str=="hi"):
        voice("hello, nice to meet you")
    if (str=="who created you"):
        voice("i was created by those 4 people standing next to you")
    if (str=="how do you do"):
        voice("i'm doing fine, thanks how are you ")
    if (str=="where are you"):
        voice("I am probably inside someone's computer")
    if (str=="i love you"):
        voice("I love you too handsome")
    if (str=="go to hell"):
        voice("perhaps i have already been there")
    if (str=="what do you do"):
        voice("i can recognize and carry out basic voice commands, and predict your expenses with help of machine learning")
    if (str=="what can you do"):
        voice("i can recognize and carry out basic voice commands, and predict your expenses with help of machine learning")
    if (str=="search *"):
        voice("okay what do you want to search")
    if (str=="check notifications"):
        voice("you have no new notifications")
    if (str=="play music"):
        voice("playing music")
    if (str=="who am i"):
        voice("i'm sorry, what is your name")
    if (str=="what is my name"):
        voice("i'm sorry, what is your name")
    if (str=="how is the weather"):
        voice("32 degree celcius with chances of rain")
    if (str=="set a reminder"):
        voice("ok, what should i remind you of")
    if (str=="count to 10"):
        voice("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    if (str=="toss a coin"):
        import random
        x = random.randint(0,1)
        if (x==0):
            print "Head"
        else:
            print "Tail"
    if (str=="im confused"):
        voice("lets toss a coin")
    if (str=="i am sad"):
        voice("hi sad, my name is Bucky ha ha ha")
    if (str==""):
        voice("I am Bucky, the new age personal assitant")
    if (str=="time"):
        voice(time.strftime('%X %x %Z'))
    if (str=="who are you"):
        voice("I am Bucky, your personal assitant")
    else:
        client = wolframalpha.Client("K9RLXP-GKPWYPR92J")
        res = client.query('sum of sqaure of 2 and square of  5')
        voice(next(res.results).text)



r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            #print value   #added by abhi
            voice("You said {}".format(value))
            reply(value)



#engine = pyttsx.init()
#           engine.say("You said {}".format(value))
#            engine.runAndWait()


            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
