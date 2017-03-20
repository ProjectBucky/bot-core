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
