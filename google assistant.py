import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import requests
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import ctypes
import time
import shutil  # Added missing import
from urllib.request import urlopen

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    global assname
    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you, sir?")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("How can I help you, Sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return "None"
    
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    assname = "Jarvis 1 point o"

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding!")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random_song = os.path.join(music_dir, random.choice(songs))
            os.startfile(random_song)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send it to?")
                to = input()
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, thank you")
            speak("How are you, Sir?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "").strip()
            assname = query
            speak(f"Name changed to {assname}")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assname)
            print(f"My friends call me {assname}")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Gaurav.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            app_id = "Wolframalpha api id"  # Replace with actual API key
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "").strip()
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk, then definitely you're human.")

        elif "why you came to world" in query:
            speak("Thanks to Gaurav. Further, it's a secret")

        elif 'power point presentation' in query:
            speak("Opening PowerPoint presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is the 7th sense that destroys all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")

        elif 'reason for you' in query:
            speak("I was created as a minor project by Mister Gaurav")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:
            try:
                api_key = "Your NewsAPI key"  # Replace with actual API key
                url = f'https://newsapi.org/v2/top-headlines?apiKey={api_key}&country=in'
                response = requests.get(url)
                data = response.json()
                i = 1
                speak('Here are some top news')
                print('=============== TOP NEWS ============' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold on a sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time do you want to stop Jarvis from listening?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "").strip()
            location = query
            speak("Locating")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all applications are closed before signing out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should I write, sir?")
            note = takeCommand()
            with open('jarvis.txt', 'w') as file:
                speak("Should I include date and time?")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime + " :- " + note)
                else:
                    file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            with open("jarvis.txt", "r") as file:
                notes = file.read()
            print(notes)
            speak(notes)

        elif "update assistant" in query:
            speak("After downloading the file, please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)
            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size=2391975), expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "jarvis" in query:
            wishMe()
            speak("Jarvis 1 point o at your service, Mister")
            speak(assname)

        elif "weather" in query:
            api_key = "Your OpenWeatherMap API key"  # Replace with actual API key
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            city_name = takeCommand()
            complete_url = f"{base_url}appid={api_key}&q={city_name}"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(f"Temperature (in Kelvin) = {current_temperature}\nPressure (in hPa) = {current_pressure}\nHumidity (in %) = {current_humidity}\nDescription = {weather_description}")
                speak(f"Temperature is {current_temperature} Kelvin, Pressure is {current_pressure} hPa, Humidity is {current_humidity} percent, and Description is {weather_description}")
            else:
                speak("City Not Found")

        elif "send message" in query:
            account_sid = 'Account Sid key'  # Replace with actual SID
            auth_token = 'Auth token'  # Replace with actual token
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=takeCommand(),
                from_='Sender No',  # Replace with actual sender number
                to='Receiver No'  # Replace with actual receiver number
            )
            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm " + query)
            speak("How are you, Mister?")
            speak(assname)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about that; maybe you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("API_ID")  # Replace with actual API ID
            res = client.query(query)
            try:
                answer = next(res.results).text
                print(answer)
                speak(answer)
            except StopIteration:
                print("No results")
