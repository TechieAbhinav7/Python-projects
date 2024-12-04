import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    # Check if the command matches specific keywords (in lowercase)
    if "open google" == c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google now.")
    
    elif "open chatgpt" == c.lower():
        webbrowser.open("https://chatgpt.com")
        speak("Opening ChatGPT now.")
    
    elif "open linkedin" == c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn now.")
    
    elif "open tube" == c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube now.")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    else:
        speak("Command not recognized.")  # If the command doesn't match any of the above

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:

        # Listen for the wake word "jarvis"
        # Obtain audio from the microphone                                                                             
        r = sr.Recognizer() 
        try:                                                                                  
            with sr.Microphone() as source:                                                                       
                print("Listening...")                                                                                   
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            print("Recognizing...")
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yeah")
                # Listen for command
                with sr.Microphone() as source:                                                                       
                    print("Jarvis Active...")
                    audio = r.listen(source) 
                    command = r.recognize_google(audio)                                                                                  
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))


