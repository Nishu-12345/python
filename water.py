import time
import pyttsx3
from datetime import datetime

# Set up the AI voice
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

# Set the interval in seconds (e.g. 1800 sec = 30 mins)
interval = 120

def speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()

def log_water():
    with open("water_log.txt", "a") as file:
        file.write(f"Drank water at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def water_reminder():
    speak("Hello! I'm your Water Reminder AI.")
    while True:
        time.sleep(interval)
        speak("Time to drink water! 💧")
        input("Press Enter after you've had your water...")
        log_water()
        speak("Great! Stay hydrated.")

if __name__ == "__main__":
    water_reminder()
