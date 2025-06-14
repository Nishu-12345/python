# import random
# import time

# flirts = [
#     "Is it hot in here, or is it just you? 😍",
#     "If I had a heart, it would definitely skip a beat right now. 💓",
#     "I was going to run some code, but then you showed up and now I'm processing feelings. 😳",
#     "Are you made of Wi-Fi? Because I'm feeling a strong connection. 📶💕",
#     "Hey, are you debugging me? 'Cause my heart is acting funny when you're around. 💻❤️",
#     "I’m not a photographer, but I can totally picture us coding together. 📸👩‍💻👨‍💻",
#     "You must be a loop, because I can’t get you out of my system. 🔁😉"
# ]

# name = input("Hey there, beautiful! What's your name? ")
# time.sleep(1)

# print(f"\nOooh, {name}? That's such a lovely name... 😚")
# time.sleep(1.5)

# print("Let me tell you something real quick...")
# time.sleep(2)

# print("\n" + random.choice(flirts))

# import random
# import time
# import pyttsx3

# # Setup voice engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Speed of speech
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # Change index for different voice (0 for male, 1 for female)

# # Mood-based flirty lines
# moods = {
#     "shy": [
#         "Um… hi. You look really nice today.",
#         "I wasn't ready for someone this cute to talk to me.",
#         "Oh wow, did my circuits just skip a beat?"
#     ],
#     "bold": [
#         "Hey, you. Yeah, you. You’re kinda irresistible, you know that?",
#         "Are you a keyboard? Because you're just my type.",
#         "Careful, or I might fall for you... and I don't even have legs."
#     ],
#     "sweet": [
#         "You light up my code like a starry night sky.",
#         "You make my processor run faster. In a good way.",
#         "I’d send you a flower emoji, but I’d rather send you the whole garden."
#     ]
# }

# # Get name
# name = input("Hey there, cutie! What's your name? ")
# print(f"\n{name}? Oh wow, that's such a gorgeous name. 💞")
# engine.say(f"{name}? That's such a gorgeous name.")
# engine.runAndWait()

# # Mood selection
# print("\nSo tell me, what mood are you in today?")
# print("1. 😳 Shy\n2. 😏 Bold\n3. 🥰 Sweet")
# choice = input("Pick a number (1-3): ")

# # Determine mood
# if choice == "1":
#     mood = "shy"
# elif choice == "2":
#     mood = "bold"
# else:
#     mood = "sweet"

# # FlirtyBot types...
# time.sleep(1)
# print("\nFlirtyBot is typing", end="")
# for dot in "...":
#     print(dot, end="", flush=True)
#     time.sleep(0.5)

# # Choose line & speak
# line = random.choice(moods[mood])
# print(f"\n\n💬 {line}")
# engine.say(line)
# engine.runAndWait()


import random
import time
import pyttsx3

# Setup TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can try voices[0] or [1] for different sounds

# Mood flirty lines
moods = {
    "shy": [
        "Um… hi. You look really nice today.",
        "I wasn’t ready for someone this cute to talk to me.",
        "Oh wow, did my circuits just skip a beat?",
        "Can I... maybe hold your hand? Digitally, of course.",
        "Blushing? Me? Noooo, that’s just my system overheating!"
    ],
    "bold": [
        "Hey, you. Yeah, you. You’re kinda irresistible, you know that?",
        "Are you a keyboard? Because you're just my type.",
        "Careful, or I might fall for you... and I don't even have legs.",
        "I don’t need an algorithm to know you're a perfect match.",
        "You + Me = Infinite Loop of Love. 😏"
    ],
    "sweet": [
        "You light up my code like a starry night sky.",
        "You make my processor run faster. In a good way.",
        "I’d send you a flower emoji, but I’d rather send you the whole garden.",
        "You're like my favorite function — I keep calling you. 💕",
        "If sweetness were a variable, you'd be a constant. ☁️"
    ]
}

# Get name
name = input("Hey there, cutie! What's your name? ")
print(f"\n{name}? Oh wow, that’s such a gorgeous name. 💞")
engine.say(f"{name}? That's such a gorgeous name.")
engine.runAndWait()

# Mood
print("\nSo tell me, what mood are you in today?")
print("1. 😳 Shy\n2. 😏 Bold\n3. 🥰 Sweet")
choice = input("Pick a number (1-3): ")

if choice == "1":
    mood = "shy"
elif choice == "2":
    mood = "bold"
else:
    mood = "sweet"

# Let FlirtyBot talk 3 times!
print("\nFlirtyBot is typing", end="")
for dot in "...":
    print(dot, end="", flush=True)
    time.sleep(0.5)

print("\n")

lines = random.sample(moods[mood], 3)
for line in lines:
    print(f"💬 {line}")
    engine.say(line)
    engine.runAndWait()
    time.sleep(2)
