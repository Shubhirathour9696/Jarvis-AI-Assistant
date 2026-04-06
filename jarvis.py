# JARVIS WITH VOICE - STEP 7 COMPLETE
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

print("🔊 VOICE JARVIS LOADING...")

class VoiceJarvis:
    def __init__(self):
        # Text-to-Speech
        self.tts = pyttsx3.init()
        voices = self.tts.getProperty('voices')
        if len(voices) > 1:
            self.tts.setProperty('voice', voices[1].id)  # Female
        self.tts.setProperty('rate', 170)
        
        # Speech-to-Text
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Calibrate mic
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        
        print("✅ VOICE JARVIS READY!")
        self.speak("Voice JARVIS activated!")
    
    def speak(self, text):
        print(f"🤖 JARVIS: {text}")
        self.tts.say(text)
        self.tts.runAndWait()
    
    def listen(self):
        try:
            print("👂 Listening...")
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
            
            text = self.recognizer.recognize_google(audio).lower()
            print(f"🎤 You said: {text}")
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            self.speak("Speech service down")
            return ""
        except:
            return ""
    
    def process(self, command):
        if "time" in command:
            now = datetime.datetime.now()
            return f"Current time {now.strftime('%I:%M %p')}"
        
        if "date" in command:
            now = datetime.datetime.now()
            return f"Today {now.strftime('%B %d')}"
        
        if "notepad" in command:
            os.system("notepad")
            return "Opening notepad"
        
        if "calculator" in command:
            os.system("calc")
            return "Opening calculator"
        
        if "google" in command:
            webbrowser.open("https://google.com")
            return "Opening Google"
        
        if "youtube" in command:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube"
        
        if "joke" in command:
            jokes = ["Why programmers hate nature? Too many bugs!"]
            return random.choice(jokes)
        
        return "Try time, date, notepad, calculator, google, youtube, joke"
    
    def run(self):
        self.speak("Say JARVIS then command")
        
        while True:
            command = self.listen()
            
            if "jarvis" in command:
                self.speak("Yes sir?")
                response = self.process(command)
                self.speak(response)

# RUN
if __name__ == "__main__":
    jarvis = VoiceJarvis()
    jarvis.run()
