import datetime
import wikipedia
import webbrowser
import os
from src.helper import greet,takeCommand,speak

if __name__ == "__main__":

    greet()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
                
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")
            
        
        elif "google" in query:
            speak("Opening google")
            webbrowser.open("google.com")
            
        
        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
            
            
        elif 'relax' in query:
            speak("Alright!. Call me if needed, have a great day!. bye for now! ")
            exit()