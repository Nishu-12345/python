# -*- coding: utf-8 -*-
import time
import random
import os
import sys
import io

# Force UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Get birthday person's name
name = input("🎉 Who's the birthday star? Enter their name: ")

# Clear screen function for cross-platform
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Balloons
balloons = [
    "🎈","🎈🎈","🎈🎈🎈","🎈🎈🎈🎈","🎈🎈🎈🎈🎈",
    "🎈🎈🎈🎈🎈🎈","🎈🎈🎈🎈🎈🎈🎈"
]

# Emojis and messages
emojis = ["🎂", "🎈", "💖", "✨", "🍬", "🍫", "🌹", "💝", "🥰", "🎉", "🎁"]
messages = [
    f"Happy Birthday, {name}!",f"Wishing you love and laughter 💖:\n",f"May all your dreams come true 🌈:\n",f"Time to party, {name}! 🎊:\n",f"You're amazing and awesome! 🥳:\n","Let's eat cake! 🎂:\n","Smile big today 😄:\n"
]
# 🎊 Animation loop with floating balloons
def float_balloons():
    for i in range(10):  # Run 10 animation cycles for balloons
        clear()  # Clear screen each time for a fresh animation frame
        print("\n" * random.randint(1, 5))  # Random space padding for some fun
        space = " " * random.randint(0, 30)  # Random horizontal space for drift
        print(f"{space}{random.choice(balloons)}")  # Display balloons floating up
        time.sleep(0.5)  # Time delay for animation smoothness

# 🎉 Main celebration animation loop
for i in range(30):
    clear()
    print("\n" * random.randint(1, 5))  # Random top padding
    space = " " * random.randint(0, 40)  # Random horizontal space
    print(space + random.choice(emojis) + "  " + random.choice(messages))
    time.sleep(0.3)

# 🎈 Final Balloon and Birthday Message
clear()
print("\n" * 3)
print("🎈🎈🎈 " * 4)
float_balloons()  # Run the floating balloon animation
print("\n" * 3)

# Final birthday message with balloons
print("💖✨🎂🎈🎉🎁 " * 3)
print(f"\n HAPPY BIRTHDAY, {name.upper()}! 🎉💖")
print("💖✨🎂🎈🎉🎁 " * 3)
print("\n" * 2)
