import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import random
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

import google.generativeai as genai

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")


def ai(prompt):
    text = f"Gemini response for Prompt: {prompt}\n******************\n\n"

    try:
        response = model.generate_content(prompt)
        print(response.text)
        text += response.text


        if not os.path.exists("Gemini"):
            os.mkdir("Gemini")

        with open(f"Gemini/prompt-{random.randint(1, 999999)}.txt", "w") as f:
            f.write(text)

        say(response.text)

    except Exception as e:
        print("Error using Gemini:", e)
        say("Sorry, I had trouble answering that.")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")
            return query
        except Exception as e:
            return "Couldn't hear you buddy, please come again"


if __name__ == "__main__":
    print('VS code running')
    say("Hello i am Buddy A.I. , How can I help you")
    while True:
        print("Listening...")
        query=takeCommand()
        if query.lower().startswith("open "):
            site_name = query[5:].strip() 

            if '.' in site_name:
                url = f"https://{site_name}"
            else:
                url = f"https://www.{site_name}.com"

            say(f"Opening {site_name} sir...")
            webbrowser.open(url)
        if "play the song" in query.lower() and "by" in query.lower():
            parts = query.lower().split("by")
            song = parts[0].replace("play the song", "").strip()
            artist = parts[1].strip()
            search_query = f"{song} {artist}".replace(" ", "%20")
            url = f"https://open.spotify.com/search/{search_query}"
            say(f"Playing {song} by {artist} on Spotify")
            webbrowser.open(url)
        if "what is the time buddy" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"buddy, the time is {strfTime}")
        if "using gemini" in query.lower():
            cleaned_prompt = query.lower().replace("using gemini", "").strip()
            ai(prompt=cleaned_prompt)
        if "hi buddy" in query.lower():
            ai(prompt=query)
        if any(exit_phrase in query for exit_phrase in ["goodbye buddy", "exit", "close buddy", "sign off buddy"]):
            say("Goodbye! Shutting down Buddy A.I.")
            break
        else:
            ai(prompt=query)
