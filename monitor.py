import pyttsx3
import time
import ctypes
import win32api

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Function to speak
def speak(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()

# Get idle duration in seconds
def get_idle_duration():
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("dwTime", ctypes.c_uint)]
    
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    millis = win32api.GetTickCount() - lii.dwTime
    return millis / 1000.0

# Monitor Alarm Main Loop
def monitor_alarm(idle_threshold=60):  # 5 minutes
    speak("Monitor alarm is now active.")
    while True:
        idle_time = get_idle_duration()
        print(f"Idle for {int(idle_time)} seconds.")
        if idle_time > idle_threshold:
            speak("Alert! You have been idle for too long.")
            time.sleep(10)  # wait before next check
        else:
            time.sleep(30)

if __name__ == "__main__":
    monitor_alarm()
