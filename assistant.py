import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

# Recognizer
listener = sr.Recognizer()

# Voice engine
engine = pyttsx3.init()


# Assistant speaking
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Listening function
def take_command():

    try:
        with sr.Microphone() as source:

            print("Listening...")

            voice = listener.listen(source)

            command = listener.recognize_google(voice)

            command = command.lower()

            print(command)

            return command

    except:
        return ""


# Main assistant function
def run_assistant():

    command = take_command()

    # Open YouTube
    if 'open youtube' in command:

        talk('Opening YouTube')

        webbrowser.open('https://youtube.com')

    # Open Google
    elif 'open google' in command:

        talk('Opening Google')

        webbrowser.open('https://google.com')

    # Play songs
    elif 'play' in command:

        song = command.replace('play', '')

        talk('Playing ' + song)

        pywhatkit.playonyt(song)

    # Tell time
    elif 'time' in command:

        time = datetime.datetime.now().strftime('%I:%M %p')

        talk('Current time is ' + time)

    # Wikipedia search
    elif 'who is' in command:

        person = command.replace('who is', '')

        info = wikipedia.summary(person, 2)

        print(info)

        talk(info)

    else:

        talk('Please say the command again')


# Infinite loop
while True:

    run_assistant()