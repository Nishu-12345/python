import tkinter as tk
from tkinter import Toplevel, scrolledtext
import random
from datetime import datetime
import pyttsx3

# 🎙️ Text-to-speech
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 🎯 Detect mood and give response
def detect_mood(user_input):
    mood = "unknown"
    mood_input = user_input.lower()

    if "sad" in mood_input or "tired" in mood_input:
        mood = "sad"
    elif "happy" in mood_input or "good" in mood_input:
        mood = "happy"
    elif "angry" in mood_input or "frustrated" in mood_input:
        mood = "angry"
    elif "anxious" in mood_input or "nervous" in mood_input:
        mood = "anxious"
    elif "scared" in mood_input:
        mood = "scared"

    responses = {
        "happy": [
            "Keep shining, sunshine!",
            "Your joy is contagious.",
            "Stay happy and spread love!"
        ],
        "sad": [
            "You’re stronger than you know.",
            "Bad days happen, but so do better ones.",
            "Crying is okay, and I’m still here for you."
        ],
        "angry": [
            "Take a deep breath. You're in control.",
            "Let’s not bottle it up. Talk to me.",
            "It's okay to feel this. You're human."
        ],
        "anxious": [
            "Inhale… exhale… you’re doing fine.",
            "It’s okay to slow down. One step at a time.",
            "You’re not alone in this feeling."
        ],
        "scared": [
            "You are brave, even when you're scared.",
            "I'm here for you, no matter what.",
            "Fear doesn’t define you — courage does."
        ],
        "unknown": [
            "I might not understand perfectly, but I care."
        ]
    }

    return mood, random.choice(responses[mood])

# 📥 Handle user input
def handle_input():
    user_text = input_field.get()
    if user_text.strip() == "":
        response_label.config(text="Please tell me how you're feeling. 💬")
        speak("Please tell me how you're feeling.")
        return

    mood, response = detect_mood(user_text)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    response_label.config(text=response)
    speak(response)

    with open("mood_history.txt", "a") as file:
        file.write(f"{now} | Mood: {mood.title()} | Input: {user_text}\n")

    input_field.delete(0, tk.END)

# 📖 View mood history
def view_history():
    history_window = Toplevel(window)
    history_window.title("Mood History 💭")
    history_window.geometry("400x300")
    history_window.configure(bg="#fff0f5")

    text_area = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, font=("Arial", 10))
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

    try:
        with open("mood_history.txt", "r") as file:
            text_area.insert(tk.END, file.read())
    except FileNotFoundError:
        text_area.insert(tk.END, "No mood history found yet. 💌")

# 🎨 GUI setup
window = tk.Tk()
window.title("MoodMate 💖")
window.geometry("450x550")
window.configure(bg="#fff0f5")

# 🖼️ MoodMate image (change filename to your actual image)
try:
    moodmate_img = tk.PhotoImage(file="moodmate.py")
    image_label = tk.Label(window, image=moodmate_img, bg="#fff0f5ff")
    image_label.pack(pady=10)
except Exception as e:
    # Fallback face if image not found
    face_label = tk.Label(window, text="(｡♥‿♥｡)", font=("Arial", 30), bg="#fff0f5")
    face_label.pack(pady=10)

# 💬 Prompt
prompt_label = tk.Label(window, text="Hi! How are you feeling today?", font=("Arial", 12), bg="#fff0f5")
prompt_label.pack()

# 📝 Input field
input_field = tk.Entry(window, width=40)
input_field.pack(pady=10)

# ✅ Submit button
submit_button = tk.Button(window, text="Tell MoodMate", command=handle_input, bg="#ffb6b6", font=("Arial", 10))
submit_button.pack(pady=5)

# 📖 View History button
history_button = tk.Button(window, text="View Mood History", command=view_history, bg="#dda0dd", font=("Arial", 10))
history_button.pack(pady=5)

# 🧠 MoodMate response
response_label = tk.Label(window, text="", wraplength=350, font=("Arial", 12), bg="#fff0f5", fg="#333")
response_label.pack(pady=20)

window.mainloop()
