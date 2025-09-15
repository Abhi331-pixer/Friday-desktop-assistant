import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests



recognizer=sr.Recognizer()
engine=pyttsx3.init()
category = "technology","general"
newsapi="db723a198a4b645e32ae325f1b9518c2"

def speak(text):
    engine.say(text)
    engine.runAndWait()
   
    
    
def processCommand(c):
    #----------website section------------------
    if "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://www.linkedin.com")
        #----------music section------------------
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
        #----------news section------------------
    elif "news" in c.lower():
        speak("opening news")
        r= requests.get("https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=in&max=10&apikey=db723a198a4b645e32ae325f1b9518c2")
        
# Check if the request was successful
    if r.status_code == 200:
        data = r.json()
        
        # Loop through articles and print headlines
        print(f"\nTop Headlines in '{category}' category:\n")
        for index, article in enumerate(data.get("articles", []), start=1):
            print(f"{index}. {article.get('title')}")
    else:
        print(f"Error fetching news: {r.status_code} - {r.text}")

if __name__ =="__main__":
     speak("Initialize Friday.....")
while True:
        #Listen for wake word"friday"
        #obtain audio from the microphone
        r = sr.Recognizer()
        print("recogniger")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower() == "friday"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("dexdude Active....")
                    audio = r.listen(source,timeout=20, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except Exception as e:
            print("Google error; {0}".format(e))

       