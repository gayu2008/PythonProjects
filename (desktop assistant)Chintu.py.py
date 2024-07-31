import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3
import pywhatkit
import os
import pyautogui
import sys

WAKE_WORD = "Hey chitti"
TERMINATION_COMMAND = "bye"

def text_to_speech(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    greeting = ''

    if 0 <= hour < 12:
        greeting = "Kaalai vanakkam Boss"
    elif 12 <= hour <= 16:
        greeting = "mathiya vanakkam Boss"
    elif 16 <= hour <= 19:
        greeting = "maalai vanakkam Boss"
    else:
        greeting = "Goodnight, Boss"

    full_message = f"{greeting}, How can I help you?"
    text_to_speech(full_message)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7)

    try:
        print("Wait for a few moments...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query.lower()

    except Exception as e:
        print("An error occurred:", e)
        text_to_speech("Sorry, I couldn't understand. Please try again.")
        return "none"

def open_website(url):
    webbrowser.open(url)

def check_wake_word():
    while True:
        query = takecommand()
        if query.lower() == WAKE_WORD.lower():
            return True
        else:
            text_to_speech("Sorry, the wake word is incorrect. Please say 'Hey chitti' to start.")

print("Listening for a wake word...")
while not check_wake_word():
    pass

print("Wake word detected! How can I assist you?")

while True:
    query = takecommand()

    if query.lower() == TERMINATION_COMMAND.lower():
        text_to_speech("Goodbye, Boss!")
        break

    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        text_to_speech(f"Boss, the time is {strTime}")

    elif 'wikipedia' in query:
        text_to_speech('Searching Wikipedia...')
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            text_to_speech("According to Wikipedia...")
            print(results)
            text_to_speech(results)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"DisambiguationError: {e}")
            text_to_speech("Sorry, I couldn't find a specific result on Wikipedia.")
        except wikipedia.exceptions.PageError as e:
            print(f"PageError: {e}")
            text_to_speech("Sorry, I couldn't find any information on Wikipedia.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            text_to_speech("Sorry, an unexpected error occurred while processing your request.")

    elif 'open youtube' in query:
        open_website("https://www.youtube.com")

    elif 'play' in query:
        query = query.replace('play', '')
        text_to_speech('Playing ' + query)
        pywhatkit.playonyt(query)
        break

    elif 'close youtube' in query:
        pyautogui.hotkey('ctrl', 'shift', 'w')

    elif 'open google' in query:
        text_to_speech("Opening Google Boss")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        while True:
            chrome_query = takecommand().lower()

            if "search" in chrome_query:
                search_query = chrome_query.replace("search", "")
                pywhatkit.search(search_query)
                text_to_speech(f'Searching for {search_query}')
            elif "close google" in chrome_query or "exit chrome" in chrome_query or "exit google" in chrome_query or "close window" in chrome_query:
                pyautogui.hotkey('ctrl', 'shift', 'w')
                text_to_speech("Closing Google Boss")
                break

            elif TERMINATION_COMMAND.lower() in chrome_query:
                text_to_speech("Goodbye, Boss!")
                sys.exit()

    elif TERMINATION_COMMAND.lower() in query:
        text_to_speech("Goodbye, Boss!")
        break
