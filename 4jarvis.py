# followed this tutorial https://www.youtube.com/watch?v=x8xjj6cR9Nc
# can't download PyObjC
import speech_recognition as sr
from time import ctime
import webbrowser
import time
from gtts import gTTS #what we pass in as text, it will create audio file and speak back to us.
import playsound
import os #remove method, remove file, google gTTS create audio file, unless remove file in code, just pile up
#os module, remove method that remove file
import random #randomely generate name for file


r = sr.Recognizer() #recognizer class, recognizes the speech

def record_audio(ask = False):  #optional, ask=False
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try: 
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('sorry, I did not get that')
        
        except sr.RequestError:
            alexis_speak('sorry, my speech service is down')
        
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is jarvis')
    
    if 'time' in voice_data:
        alexis_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of' + location)

    if 'exit' or 'bye' in voice_data:
        exit()


time.sleep(1)
alexis_speak('how can I help you?')
while 1: #wait for us to talk
    voice_data = record_audio()
    respond(voice_data)
