import pyttsx3
friend = pyttsx3.init() #initialize
speech = input('Say something:')
friend.say(speech)
friend.runAndWait() #runs an event loop until all commands queued up until this