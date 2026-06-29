# Jarvis - Voice Activated Virtual Assistant

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import time

# API Keys
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    try:
        tts = gTTS(text=text, lang="en")
        filename = "temp.mp3"

        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()

        # Wait before deleting
        time.sleep(1)

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print("Speak Error:", e)


def aiProcess(command):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-5.4",
            messages=[
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant. Give short answers."
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI Error: {e}"


def processCommand(command):

    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")

    elif command.startswith("play"):

        parts = command.split(maxsplit=1)

        if len(parts) < 2:
            speak("Please tell me a song name.")
            return

        song = parts[1]

        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak("Song not found in music library.")

    elif "news" in command:

        try:
            url = (
                f"https://newsapi.org/v2/top-headlines?"
                f"country=in&apiKey={NEWS_API_KEY}"
            )

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                articles = data.get("articles", [])

                if not articles:
                    speak("No news found.")
                    return

                speak("Here are the latest headlines.")

                for article in articles[:5]:
                    speak(article["title"])

            else:
                speak("Unable to fetch news.")

        except Exception as e:
            print("News Error:", e)

    else:
        reply = aiProcess(command)
        print("Jarvis:", reply)
        speak(reply)


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        try:
            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening for wake word...")
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            wake_word = recognizer.recognize_google(audio)

            print("You said:", wake_word)

            if wake_word.lower() == "jarvis":

                speak("Yes Sir")

                with sr.Microphone() as source:

                    print("Jarvis Active...")
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=10
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            continue

        except sr.UnknownValueError:
            continue

        except Exception as e:
            print("Error:", e)