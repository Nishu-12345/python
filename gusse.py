import random

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Ask if user wants to enable cheat mode
cheat = input("Do you want to enable cheat mode? (yes/no): ").lower()

# Generate a random number between 1 and 100
secret_number = random.randint(1, 10)

# If cheat mode is on, show the secret number
if cheat == 'yes':
    print(f"[CHEAT MODE] The secret number is: {secret_number}")

guess = None  # Initialize guess variable
attempts = 0  # Count how many tries the user takes

# Game loop
while guess != secret_number:
    # Ask the user for a guess
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts 🎉")

