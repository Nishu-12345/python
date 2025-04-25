import random
import time

# Magical title with ASCII
def print_welcome():
    print(r"""
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __  __ _ _ __ ___   ___
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '| | | |_ |/ ` | ' ` _ \ / _ \
 | |\  | || | | | | | | |) |  _/ |    | || | (| | | | | | |  __/
 || \|\,|| || ||./ \||     \|\,|| || ||\_|
                                                                      
""")
    print("✨ Welcome to the Number Guessing Game! ✨")
    print("I'm thinking of a number between 1 and 10...\n")

# Dramatic cheat mode activation
def activate_cheat_mode(secret_number):
    print("\n🧙‍♂✨ A strange wind blows...")
    time.sleep(1)
    print("🌌 The stars align...")
    time.sleep(1)
    print("📜 The secret scroll reveals a number...")
    time.sleep(1.5)
    print(f"\n💥 [CHEAT MODE ACTIVATED] The secret number is: {secret_number} 💥\n")

# Start of the game
print_welcome()

# Ask for secret code
secret_code = input("Enter a secret code (or just press Enter to skip): ").lower()
secret_number = random.randint(1, 100)

# Handle cheat mode
if secret_code == 'wizard':
    activate_cheat_mode(secret_number)
else:
    print("🕵 No magic detected. Let's play fair... or is there a hidden word? 🤫\n")

# Guessing loop
guess = None
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("⬆ Too low! Try again.\n")
        elif guess > secret_number:
            print("⬇ Too high! Try again.\n")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts! 🎉\n")
    except ValueError:
        print("⚠ Please enter a valid number!\n")