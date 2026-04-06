"""
JARVIS AI ASSISTANT - COMPLETE ONE-FILE SOLUTION
Just run: python jarvis.py
Works on Windows/Mac/Linux
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import requests
import random
import sys
import json

class Jarvis:
    def __init__(self):
        print("🚀 INITIALIZING JARVIS...")
        
        # Initialize components
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        
        # Configure voice (female voice if available)
        voices = self.tts_engine.getProperty('voices')
        if len(voices) > 1:
            self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
        self.tts_engine.setProperty('rate', 180)  # Speed
        
        # Wake words
        self.wake_words = ["jarvis", "hey jarvis", "hello jarvis"]
        
        # Calibrate microphone for better recognition
        print("🔊 Calibrating microphone...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("✅ JARVIS READY!")
        self.speak("JARVIS online and ready sir!")
    
    def speak(self, text):
        """Text to Speech"""
        print(f"🤖 JARVIS: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def listen(self):
        """Speech to Text"""
        try:
            print("👂 Listening...")
            with self.microphone as source:
                # Listen with timeout
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
            
            # Convert speech to text
            command = self.recognizer.recognize_google(audio).lower()
            print(f"🎤 You said: {command}")
            return command
            
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            self.speak("Speech recognition service unavailable")
            return ""
        except sr.WaitTimeoutError:
            return ""
    
    def is_wake_word(self, command):
        """Check if JARVIS wake word detected"""
        return any(word in command for word in self.wake_words)
    
    def get_time(self):
        """Current time"""
        now = datetime.datetime.now()
        return now.strftime("%I:%M %p")
    
    def get_date(self):
        """Current date"""
        now = datetime.datetime.now()
        return now.strftime("%B %d, %Y")
    
    def open_website(self, url):
        """Open website"""
        webbrowser.open(url)
        return f"Opening {url}"
    
    def open_app(self, app_name):
        """Open applications"""
        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "notepad": "notepad.exe"
        }
        
        if app_name in apps and os.name == 'nt':  # Windows
            try:
                os.startfile(apps[app_name])
                return f"Opening {app_name}"
            except:
                return f"Could not open {app_name}"
        else:
            return f"Sorry, can't open {app_name} on this system"
    
    def search_google(self, query):
        """Google search"""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching Google for {query}"
    
    def search_youtube(self, query):
        """YouTube search"""
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        return f"Opening YouTube for {query}"
    
    def tell_joke(self):
        """Random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the computer go to therapy? It had too many bytes of emotional baggage!"
        ]
        return random.choice(jokes)
    
    def get_weather(self, city="London"):
        """Weather info (uses free API)"""
        try:
            # Free weather API (no key needed for basic use)
            url = f"http://wttr.in/{city}?format=j1"
            response = requests.get(url).json()
            temp = response['current_condition'][0]['temp_C']
            feels = response['current_condition'][0]['FeelsLikeC']
            return f"In {city}, it's {temp}°C, feels like {feels}°C"
        except:
            return "Sorry, couldn't fetch weather right now"
    
    def process_command(self, command):
        """Main command processor"""
        command = command.lower()
        
        # Time & Date
        if "time" in command:
            return f"The current time is {self.get_time()}"
        
        if "date" in command:
            return f"Today's date is {self.get_date()}"
        
        # Weather
        if "weather" in command:
            city = "London"
            if "in" in command:
                city = command.split("in")[-1].strip()
            return self.get_weather(city)
        
        # Web
        if "google" in command or "search" in command:
            query = command.replace("google", "").replace("search", "").strip()
            return self.search_google(query)
        
        if "youtube" in command:
            query = command.replace("youtube", "").replace("play", "").strip()
            return self.search_youtube(query)
        
        # Applications
        if "open" in command:
            app = command.replace("open", "").strip()
            return self.open_app(app)
        
        # Fun
        if "joke" in command or "funny" in command:
            return self.tell_joke()
        
        # Websites
        if "facebook" in command:
            return self.open_website("https://facebook.com")
        if "github" in command:
            return self.open_website("https://github.com")
        if "stackoverflow" in command:
            return self.open_website("https://stackoverflow.com")
        
        # Exit
        if any(word in command for word in ["exit", "quit", "bye", "goodbye"]):
            return "Shutting down JARVIS. Goodbye sir!"
        
        # Default
        return "I didn't understand that command. Try: time, weather, open notepad, search, joke"
    
    def run(self):
        """Main JARVIS loop"""
        self.speak("JARVIS at your service!")
        
        while True:
            # Listen for command
            command = self.listen()
            
            # Check wake word
            if self.is_wake_word(command):
                self.speak("Yes sir?")
                
                # Process command
                response = self.process_command(command)
                self.speak(response)
                
                # Check if shutdown
                if "goodbye" in response.lower() or "shutting down" in response.lower():
                    self.speak("JARVIS signing off!")
                    break
        
        print("👋 JARVIS shutdown complete!")

def main():
    """Entry point"""
    try:
        jarvis = Jarvis()
        jarvis.run()
    except KeyboardInterrupt:
        print("\n👋 JARVIS interrupted by user!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
