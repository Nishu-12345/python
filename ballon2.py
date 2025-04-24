# -*- coding: utf-8 -*-
import time
import random
import os
import sys
import io
import platform

# For Windows beep sound
if platform.system() == "Windows":
    import winsound

# Force UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Get birthday person's name
name = input("🎉 Who's the birthday star? Enter their name: ")

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Balloons
balloons = [
    "🎈", "🎈🎈", "🎈🎈🎈", "🎈🎈🎈🎈", "🎈🎈🎈🎈🎈",
    "🎈🎈🎈🎈🎈🎈", "🎈🎈🎈🎈🎈🎈🎈"
]

# Messages
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

# Confetti
confetti = ["✨", "🎊", "💥", "🎉", "🌟", "🧨"]

# 🎈 Floating balloon animation
def float_balloons():
    for i in range(8):
        clear()
        print("\n" * random.randint(1, 5))
        space = " " * random.randint(0, 30)
        print(f"{space}{random.choice(balloons)}")
        time.sleep(0.4)

# 🎊 Confetti rain animation
def confetti_rain():
    for _ in range(10):
        clear()
        for _ in range(15):
            space = " " * random.randint(0, 40)
            print(space + random.choice(confetti))
        time.sleep(0.2)

# 🎶 Happy Birthday melody (Windows only)
def play_melody():
    if platform.system() != "Windows":
        print("🎶 (Sound not supported on this OS, but imagine the tune!) 🎵")
        return

    # Notes for "Happy Birthday"
    melody = [
        (264, 300), (264, 300), (297, 600), (264, 600), (352, 600), (330, 1200),
        (264, 300), (264, 300), (297, 600), (264, 600), (396, 600), (352, 1200),
        (264, 300), (264, 300), (528, 600), (440, 600), (352, 600), (330, 600), (297, 1200),
        (466, 300), (466, 300), (440, 600), (352, 600), (396, 600), (352, 1200)
    ]

    for note, duration in melody:
        winsound.Beep(note, duration)

# 🎉 Celebration messages
for _ in range(25):
    clear()
    print("\n" * random.randint(1, 5))
    space = " " * random.randint(0, 35)
    print(space + random.choice(emojis) + "  " + random.choice(messages))
    time.sleep(0.3)

# 🎈 Final effect
float_balloons()
confetti_rain()

# # 🎶 Play song
# print(f"\n🎵 Playing Happy Birthday for {name}...\n")
# play_melody()

# ... [Same imports and setup as before]

# 🎶 Song lyric display
def song_lyric():
    lyric = [
        "💞 \"I have died every day waiting for you...\"",
        "💫 \"Darling, don't be afraid, I have loved you...\"",
        "🌙 \"For a thousand years...\"",
        "🎵 \"I'll love you for a thousand more.\""
    ]
    for line in lyric:
        print("\n" + line.center(80))
        time.sleep(2)

# 🎉 Final sequence
float_balloons()
confetti_rain()

# 🎶 Play song
print(f"\n🎵 Playing Happy Birthday for {name}...\n")
play_melody()

# 💖 Song dedication
clear()
print("\n" * 3)
print("💖 A Special Lyric Just For You 💖\n".center(80))
song_lyric()

# 🎆 Final birthday message
print("\n" * 2)
print("💖✨🎂🎈🎉🎁 " * 3)
print(f"\n       🎉🎉🎉  HAPPY BIRTHDAY, {name.upper()}! 🎉🎉🎉")
print("💖✨🎂🎈🎉🎁 " * 3)
print("\n" * 2)

# 🎆 Final birthday message
# clear()
# print("💖✨🎂🎈🎉🎁 " * 3)
# print(f"\n       🎉🎉🎉  HAPPY BIRTHDAY, {name.upper()}! 🎉🎉🎉")
# print("💖✨🎂🎈🎉🎁 " * 3)
# print("\n" * 2)
print(f"\nFrom someone who’ll always be by your side, no matter what. ❤️\n")
