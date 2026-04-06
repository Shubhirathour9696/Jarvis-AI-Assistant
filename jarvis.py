# STEP 3 - CORE JARVIS (100% WORKING)
import pyttsx3
import datetime
import webbrowser
import os
import sys

class Jarvis:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        print("🤖 CORE JARVIS v1.0 LOADED!")
        self.speak("Core JARVIS online!")
    
    def speak(self, text):
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def run(self):
        self.speak("Commands ready: time, date, notepad, calculator, google, youtube, joke, exit")
        
        while True:
            cmd = input("\n👤 Say: ").lower()
            
            if "time" in cmd:
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"Current time {time_now}")
            
            elif "date" in cmd:
                date_now = datetime.datetime.now().strftime("%B %d, %Y")
                self.speak(f"Today is {date_now}")
            
            elif "notepad" in cmd:
                os.system("notepad")
                self.speak("Opening Notepad")
            
            elif "calculator" in cmd or "calc" in cmd:
                os.system("calc")
                self.speak("Opening Calculator")
            
            elif "google" in cmd:
                webbrowser.open("https://www.google.com")
                self.speak("Opening Google")
            
            elif "youtube" in cmd:
                webbrowser.open("https://www.youtube.com")
                self.speak("Opening YouTube")
            
            elif "joke" in cmd:
                self.speak("Why don't programmers like nature? Too many bugs!")
            
            elif "exit" in cmd or "quit" in cmd:
                self.speak("JARVIS signing off!")
                sys.exit()
            
            else:
                self.speak("Say time, date, notepad, calculator, google, youtube, joke, or exit")

# RUN
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
