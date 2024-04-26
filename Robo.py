import os
from pickle import SHORT_BINSTRING
import pyttsx3
import pyaudio
import wikipedia
import webbrowser 
import speech_recognition as sr 
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
    
def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning!")
        
        
     elif hour>=12 and hour<18:
         speak("Good Afternoon!")
         
     elif hour>=4 and hour<16:
         speak("Good evening")    
         
     else:
         speak("Good evening")
         
     speak("I am ROBo. sir Please tell me how can I assist you")           
     
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")    
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("say that again please sir.....")
        return "None"        
    return query

if __name__ == "__main__":
    speak("Hello sir")
    wishme()
    while True:
     query = takeCommand().lower()
          
     if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results) 
     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
     elif 'open facebook' in query:
         webbrowser.open("facebook.com")   
         
     elif 'open instagram' in query:
             webbrowser.open("instagram.com") 
             
     elif 'open gmail' in query:
             webbrowser.open("gmail.com")
             
     elif 'play music' in query:
             music_dir ='C:\\Users\\priyanshu\\Music'                                 
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[2]))
               
     elif 'tell me time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir,the time is {strTime}")
         print(strTime)
         
     elif 'open google' in query:
             webbrowser.open("google.com")
                 
     
                  
        
        