def moodmate():
    print("🤖 MoodMate: Hi! How are you feeling today?")
    mood = input("You: ").lower()

    if "sad" in mood or "tired" in mood:
        print("MoodMate: I'm sending you a big virtual hug. 🫂💖 You're not alone.")
    elif "happy" in mood or "good" in mood:
        print("MoodMate: Yay! I'm so glad you're feeling good. Keep shining 🌞")
    elif "angry" in mood or "frustrated" in mood:
        print("MoodMate: Deep breaths, love. You've got this. Let's handle one thing at a time. 💪")
    elif "anxious" in mood or "nervous" in mood:
        print("MoodMate: Inhale... exhale... you're stronger than you feel. 🌷 I'm with you.")
    elif"scared" in mood or "nervous" in mood:
        print("MoodMate: What, happen to you, dear.... don't scare because you're strong and I'm with you. ♾️")   
    else:
        print("MoodMate: I might not understand perfectly, but I care. 💛")
        
    print("\n🌸 MoodMate: I'm proud of you for checking in with yourself.")

moodmate()
