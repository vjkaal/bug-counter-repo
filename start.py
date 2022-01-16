#!/usr/bin/env python3

import speech_recognition as sr
import pyaudio
import pyttsx3
import subprocess
import os

# start listen and speak services

engine = pyttsx3.init("espeak")
rec = sr.Recognizer()

# other op

def chkInteger(text):
    print(text)
    if((isinstance(int(text), int) == True) and (int(text) > 0)):
        return True
    else:
        return False

def toInteger(text):
    if(text == "\n" or text == ""):
        return int(0)
    elif(isinstance(int(text), int) == True):
        return int(text)

# java execution

def executeFile(cmd):
    s = subprocess.check_output(str(cmd), shell = True)
    return s.decode("utf-8")

# file op

def clearFile():
    res = ""
    if __name__ == "__main__":
        res = executeFile("java clearFile.java")

    return res

def writeToFile(text):
    res = ""
    print(text)
    if __name__ == "__main__":
        res = executeFile("java writeToFile.java " + str(text))

    return res

def readFromFile():
    res = ""
    if __name__ == "__main__":
        res = executeFile("java readFromFile.java")
    return res

# speaker n mic op

def say(text):
    engine.say(str(text))
    engine.runAndWait()

def listen():
    res = ""
    try:
        with sr.Microphone() as source:
            print('...')
            rec.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = rec.record(source, duration=2)
            print("Recognizing your text.............")
            text = rec.recognize_google(audio_data)
            print(text)
            res = text


    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")

    return res

def ask(text):
    say(text)
    print("say yes or no")
    res = listen()
    print(res)
    return (str(res).lower() == "yes")

# starts here
input = 0
while(chkInteger(input) != True):
    say("Tell me number of bugs")
    input = listen()
    say(input)

say("now writing to file")
res = readFromFile();
res = toInteger(res)
input = toInteger(input)
print(res)
if(isinstance(input, int) == True):
    res = res + input
    say(writeToFile(res))
else: say("failed to write not a number")

if(ask("shall I read from file")):
    say("total number of bugs ")
    say(res)

if(ask("shall I clear the file")):
    say(clearFile())

say("thank you")
