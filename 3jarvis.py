#followed https://www.analyticsvidhya.com/blog/2020/11/build-your-own-desktop-voice-assistant-in-python/ 
# issue with mp3, playsound, and gTTS
# error is "1.mp3"

import speech_recognition as sr # convert speech to text
import datetime #for fetching date and time
import wikipedia 
import webbrowser
import requests
import playsound #to play saved mp3
from gtts import gTTS #google text to speech
import os #to save/open files
from selenium import webdriver #to control browser operations
#import wolframalpha to claculate strings into formulas

# function to capture my requests
def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data=""
        try:
            data = input.recognize_google(audio)
            print("Your question is, " + data)
        
        except sr.UnknownValueError:
            print('Oops, I did not hear your question. Please repeat')
    return data

#function that responds to my questions
def respond(output):
    num = 0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':
    respond('Hi, I am Jarvis, your personal desktop assistant')

    while(1):
        
        respond("How can I help you?")
        text = talk().lower()

        if text==0:
            continue

        if 'stop' in str(text) or 'exit' in str(text) or 'bye' in str(text):
            respond("ok bye")
            break

        if 'wikipedia' in text:
            respond('Searching wikipedia')
            text = text.replace('wikipedia', '')
            results = wikipedia.summary(text, sentences=3)
            respond('According to the wiki')
            print(results)
            respond(results)
        
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")
        
        elif 'search' in text:
            text = text.replace('search', '')
            webbrowser.open_new_tab(text)
            #time.sleep(5)
        
        elif 'open google' in text:
            webbrowser.open_new_tab('https://www.google.com')
            respond('Google is open')
        
        else:
            respond('app not available')



