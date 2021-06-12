import sys
import pyttsx3
import datetime
from pyttsx3 import driver
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import sys
import random
import ctypes
import requests, json
import pyautogui
import pywhatkit
import pyaudio
# from selenium import webdriver

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def weather():
    
        api_key = "c7564225bc2e86b8e8ea90f5122bac73"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Odisha"
        complete_url =base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature_in_k = y["temp"]
            current_temperature=int(current_temperature_in_k-273)
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak("The current weather looks like "+str(weather_description)+". If you want to know about the current temperature , then it is "+str(current_temperature)+" degree celcius and the humidity is "+str(current_humidiy))
            take_command()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    
    hour=datetime.datetime.now().hour
    if hour>=0 and hour <=12:
        speak("Good Morning boss !")
    elif hour>=12 and hour<=16:
        speak("Good afternoon boss !")
    elif hour>=16 and hour<=21:
        speak("Good Evening boss !")
    else:
        speak("Hello boss !")
    speak("I am Mark  . How may I help you ?")

def take_command():
    #It takes microphone inputs from the user and returns output . 
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio,language='en_in')
        print(f"User said : {command}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return command

def doing_work():
    while True :
        
        command=take_command().lower()
        if 'wikipedia' in command:
            speak("Searching Wikipedia")
            print("Searching Wikipedia....")
            command=command.replace("wikipedia","")
            results=wikipedia.summary(command,sentences=2)
            speak("According to Wikipedia , ")
            speak(results)
            print(results)
        
        elif 'doing' in command:
            speak("I am following your orders boss")

        elif 'you do' in command:
            speak("I can access all your default apps , I also can do some search for you boss . I am new in this field , If you want you can upgrade me and can do more thing by me .")

        elif 'are you there' in command or ' you hear' in command:
            speak("I am always here for you boss")

        elif 'yourself' in command or 'are you' in command or 'your name' in command:
            speak("Boss I am EDITH  , Your AI voice assistant")
        
        elif 'am i' in command or 'my name' in command:
            speak("You are my Boss Mr Amit Kumar Mallick")

        elif 'girlfriend' in command:
            speak("I think i am the only AI girl whom you like so much")
        
        elif 'search' in command or 'what is' in command or 'who is' in command:
            # googleSearch()
            print(command)
            command_search=str(command)
            command_search=command.replace("mark","")
            # command_search=command_search.replace(" in google","")
            command_search=command_search.replace("hey","")
            command_search=command_search.replace("search","")
            command_search=command_search.replace("what is","")
            command_search=command_search.replace("who is","")
            command_search=command_search.replace("who are","")
            command_search=command_search.replace("how to","")
            command_search=command_search.replace("what do you mean by","")
            command_search=command_search.replace("ok","")
            command_search=command_search.replace("no","")


            print(command_search)
            try:
                # pywhatkit.search(command)
                # url="https://en.wikipedia.org/wiki/"+str(command_search)
                # webbrowser.open(url)
                answer=wikipedia.summary(command_search,2)
                print(f"According to Google : {answer}")
                speak(f"According to Google : {answer}")
                speak("Do you want to see thi in google ?")
                if 'yes' in command or 'ok' in command:
                    wikipedia.search(command_search)

            except Exception as e:
                # print("Your answer not found in wikipedia ,Please Search here")
                speak("Your answer not found in wikipedia ,Please Search here")
        
        elif "time" in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            speak("Current time is "+time)
            print("The Current time is : "+time)
        
        elif 'date' in command:
            date=datetime.datetime.now().strftime('%d:%B:%Y')
            speak("Current date is"+date)
            print("Current date is : "+date)
        
        elif 'command' in command or 'cmd' in command:
            speak("Openeing Command prompt")
            os.startfile('cmd')        

        elif 'location' in command:
            speak("Opening map")
            webbrowser.open('https://goo.gl/maps/ALiU4AHc7mcVFcuV9')

        elif 'chrome' in command or 'browsing' in command:
            speak("Openeing Chrome")
            path='C:\\Users\\AMIT\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe '
            os.startfile(path)

        elif "open Youtube" in command or 'some video' in command:
            speak("Opening Youtube for you boss..")
            webbrowser.open_new("https://youtube.com")
        
        elif 'youtube' in command:

            speak("Searching your video in youtube boss ")
        
        elif "open google" in command:
            speak("Opening Google for you boss..")
            webbrowser.open_new("https://google.com")

        elif "open stackoverflow" in command:
            speak("Opening Stckoverflow for you boss..")
            webbrowser.open_new("https://stackoverflow.com")

        elif "open instagram" in command:
            speak("Opening instagram for you boss..")
            webbrowser.open_new_tab("https://www.instagram.com")

        elif 'open twitter' in command:
            speak("Opening Twitter for you boss..")
            webbrowser.open_new("https://twitter.com")

        elif "song" in command or 'music' in command:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            random_song=random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))

        elif "code" in command:
            path="C:\\Users\\AMIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif 'whatsapp' in command:
            speak("Opening whatsapp for you sir")
            webbrowser.open('https://web.whatsapp.com')
        
        elif 'weather' in command:
            weather()                
            
        elif 'lock' in command or 'sleep' in command:
            speak("Ok boss, going to sleep")
            ctypes.windll.user32.LockWorkStation()

        

        elif 'calculator' in command or 'calculation' in command:
            speak("Opening calculator")
            os.startfile('calc')

        elif 'notepad' in command:
            speak("Opening notepad")
            os.startfile('notepad')
               
        elif 'screenshot' in command:
            pic=pyautogui.screenshot()
            pic.save('D:\\PHOTOS\\Screenshots\\sc1.png')
            speak("I  have taken a screenshot of the current window . Do you want to check it in your screenshot folder ?")
            command=take_command().lower()
            if 'yes' in command or 'ok' in command:
                speak("Opening Scrrenshot folder")
                os.startfile('D:\\PHOTOS\\Screenshots')
            elif 'no' in command:
                speak("Okay boss")
                take_command()

        elif 'quit' in command or 'exit' in command or 'stop' in command or 'close' in command:
            hour=datetime.datetime.now().hour
            speak("On your command boss .")
            if hour>=6 and hour <=12:
                speak("Have a good day  !")
            else:
                speak("Good night  .")
            sys.exit()


if __name__=="__main__":
    speak("Hello Sir  ,  Let me know who are you !")
    # print(command)
    while True:
        command=take_command().lower()
        print(command)
        if 'kumar' in command:
            print("Entering to E.D.I.T.H ")
            speak(" EDITH activated .")
            speak(" Welcome to EDITH .")
            wish_me()
            doing_work()
        
        elif 'quit' in command or 'exit' in command or 'stop' in command or 'close' in command:
            hour=datetime.datetime.now().hour
            if hour>=0 and hour <=12:
                speak("Have a good day sir !")
            else:
                speak("Good night sir .")
            sys.exit()

        else:
            speak("Access Denied")
            # command=take_command().lower()
    

        


