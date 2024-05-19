import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

#speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()


# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            #print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
#greetings
def greet():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Kushal!. Hope your doing well!")
    
    elif hour>=12 and hour<18:
        speak("Hello Kushal!. Hope your doing well!")

    else:
        speak("Hello Kushal!. Hope your doing well!")
    
    speak("I am your assistant. How may i help you?")
    
    
    
###-------------------------- BELOW ARE FUNCTIONS FOR APP RUN ON STREAMLIT --------------------------------###



import google.generativeai as genai
from gtts import gTTS

GOOGLE_API_KEY = '******************************' # your google api key
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def voice_input():
    # Create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    

def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')  # Language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")



def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result