#a library will typically contain multiple modules.

import pyttsx3 #pip install pyttsx3 
#pyttsx3 is a text-to-speech conversion library in Python

import speech_recognition as sr #pip install speechRecognition
# Library for performing speech recognition

import datetime
#The datetime module has a class named dateclass that can contain information from both date and time objects.

import wikipedia #pip install wikipedia
#Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.

import webbrowser
#The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.

import os
#The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules.

import pyaudio
#To get started with playback and recording audio on Windows, Linux, and MacOS in a Python environment you should consider using the PyAudio library. PyAudio is a set of Python bindings for PortAudio, a cross-platform C++ library interfacing with audio drivers.

import subprocess
#The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

import webbrowser as wb

# registering browser
wb.register('chrome',None)

#########################################################################################################

# choosing voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak to me command
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wishes me good morning
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello Sir !")
    if hour>=0 and hour<12:
        speak("Good Maurning ")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")  
    elif hour>=16 and hour<20:
        speak("Gooood Evening ")   
    else:
        speak("Good Night ")  

    speak("How may I help ? ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        #print("Working on Command ...",end='')    
        query = r.recognize_google(audio, language='en-in')
        print(f" : {query}\n")
        #speak("Working on your words sir......")

    except Exception as e: 
        return "None"
    return query

############################################################################################################

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        #With the help of the takeCommand() function, our A.I. assistant will be able to return a string output by taking microphone input from us

        ############################# Logic for executing tasks based on query ##############################

        #basic questions and answers
        if 'hello jarvis' in query:
            speak('Hello sir ')
        elif 'you are lazy' in query:
            speak('sorry sir you need SSD')
        elif 'i am hungry' in query:
            speak('have some food sir')
        elif 'google' in query:
            query = query.replace("google", "")
            wb.open('query')    


        # Using wikipedia module
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)                      # this will print results on the screen
            speak(results)                      # speak the results

        # youtube 
        elif 'open youtube' in query:
            wb.open('https://www.youtube.com')

        #Study Material
        elif 'python tutorial' in query:
            wb.open('https://www.w3schools.com/python/')
        elif 'c++ tutorial' in query:
            wb.open('https://www.youtube.com/watch?v=Iuo9PpGE04Y&list=PLLYz8uHU480j37APNXBdPz7YzAi4XlQUF')

        # stackoverflow
        elif 'open stack overflow' in query:
            wb.open('https://stackoverflow.com')

        # Songs part
        elif 'play bekhayali' in query:
            wb.open('https://www.youtube.com/watch?v=VOLKJJvfAbg')
        elif 'play thodi der' in query:
            wb.open('https://www.youtube.com/watch?v=FGTv9-oQhIg')
        elif 'play ishq mubarak' in query:
            wb.open('https://www.youtube.com/watch?v=V1oczq_8L0E')
        elif 'play tu itni khubsurat hai' in query:
            wb.open('https://www.youtube.com/watch?v=PKIlSv9yMTY')

        #online programming sites
        elif 'open python ide' in query:
            wb.open('https://www.onlinegdb.com/online_python_compiler')
        elif 'open c plus plus ide' in query:
            wb.open('https://www.onlinegdb.com/online_c++_compiler')
        elif 'open cf' in query:
            wb.open('https://codeforces.com/problemset?order=BY_RATING_ASC')
        elif 'open c plus plus' in query:
            wb.open('https://www.tutorialspoint.com/compile_cpp_online.php')

        # Opening Applications
        elif 'calculator' in query:
            subprocess.call('calc.exe')
        elif 'notepad' in query:
            subprocess.call('notepad.exe')

        # Show time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)   
            speak(f"Sir, the time is {strTime}")

        # Quit Command
        elif 'thank you' in query:
            speak("Welcome Sir")
            break
 


            
