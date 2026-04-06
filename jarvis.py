# ========================================
# JARVIS AI ASSISTANT - COMPLETE WORKING VERSION
# JUST RUN: python jarvis.py
# ========================================

import pyttsx3
import datetime
import webbrowser
import os
import requests
import random
import subprocess

print("🚀 JARVIS LOADING...")

class Jarvis:
    def __init__(self):
        # Initialize Text-to-Speech
        self.tts_engine = pyttsx3.init()
        voices = self.tts_engine.getProperty('voices')
        
        # Use female voice if available
        if len(voices) > 1:
            self.tts_engine.setProperty('voice', voices[1].id)
        self.tts_engine.setProperty('rate', 170)
        
        print("✅ JARVIS VOICE READY!")
    
    def speak(self, text):
        """JARVIS SPEAKS"""
        print(f"🤖 JARVIS: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("%I:%M %p")
    
    def get_date(self):
        now = datetime.datetime.now()
        return now.strftime("%A, %B %d, %Y")
    
    def process_command(self, command):
        command = command.lower()
        
        # TIME
        if "time" in command:
            return f"Current time is {self.get_time()}"
        
        # DATE  
        if "date" in command:
            return f"Today is {self.get_date()}"
        
        # WEATHER (Simple)
        if "weather" in command:
            return "The weather is perfect for coding!"
        
        # OPEN APPS
        if "notepad" in command:
            os.system("notepad")
            return "Opening Notepad"
        
        if "calculator" in command:
            os.system("calc")
            return "Opening Calculator"
        
        # WEB SEARCH
        if "search" in command or "google" in command:
            query = command.replace("search", "").replace("google", "").strip()
            webbrowser.open(f"https://google.com/search?q={query}")
            return f"Searching Google for {query}"
        
        # YOUTUBE
        if "youtube" in command:
            query = command.replace("youtube", "").strip()
            webbrowser.open(f"https://youtube.com/results?search_query={query}")
            return f"Opening YouTube"
        
        # JOKE
        if "joke" in command:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "I'm reading a book about anti-gravity. It's impossible to put down!"
            ]
            return random.choice(jokes)
        
        # WEBSITES
        if "facebook" in command:
            webbrowser.open("https://facebook.com")
            return "Opening Facebook"
        
        if "github" in command:
            webbrowser.open("https://github.com")
            return "Opening GitHub"
        
        # EXIT
        if any(word in command for word in ["exit", "quit", "bye", "goodbye"]):
            return "JARVIS signing off! Goodbye sir!"
        
        # DEFAULT
        return "Commands: time, date, notepad, calculator, search [topic], youtube [song], joke, exit"
    
    def run(self):
        self.speak("JARVIS online and ready sir!")
        
        while True:
            print("\n" + "="*50)
            command = input("👤 YOU: ").strip()
            
            if command.lower() == "exit":
                self.speak("Goodbye sir!")
                break
            
            response = self.process_command(command)
            self.speak(response)
        
        print("👋 JARVIS OFFLINE")

# START JARVIS
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
