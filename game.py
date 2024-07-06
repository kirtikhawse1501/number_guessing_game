import random

def number_guessing_game():
    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    # Computer selects a random number between 1 and 100
    selected_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0

    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the attempt counter
        attempts += 1

        # Check if the user's guess is correct
        if guess == selected_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        # Provide a hint if the guess is too high or too low
        elif guess < selected_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
