# -*- coding: utf-8 -*-
import time
import random
import os

# Optional: make sure output uses UTF-8
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Get birthday person's name
name = input("🎉 Who's the birthday star? Enter their name: ")

# Clear screen (works on Windows/Linux/Mac)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Emojis and messages
emojis = ["🎂", "🎈", "💖", "✨", "🍬", "🍫", "🌹", "💝", "🥰", "🎉", "🎁"]
messages = [
    f"Happy Birthday, {name}!",
    f"Wishing you love and laughter 💖",
    f"May all your dreams come true 🌈",
    f"Time to party, {name}! 🎊",
    f"You're amazing and awesome! 🥳",
    "Let's eat cake! 🎂",
    "Smile big today 😄"
]

# 🎊 Animation loop
for i in range(30):
    clear()
    print("\n" * random.randint(1, 5))  # Random top padding
    space = " " * random.randint(0, 40)  # Random horizontal space
    print(space + random.choice(emojis) + "  " + random.choice(messages))
    time.sleep(0.3)

# 🎉 Final message
clear()
print("\n" * 3)
print("💖✨🎂🎈🎉🎁 " * 3)
print(f"\n        HAPPY BIRTHDAY, {name.upper()}! 🎉💖")
print("💖✨🎂🎈🎉🎁 " * 3)
print("\n" * 2)
