import random

def main():
    secret_number = random.randint(1, 10)
    print("I am thinking of a number between 1 and 10...")

    # First guess attempt, check for exit condition
    guess = get_valid_guess("Enter a guess (or press Enter to quit): ")
    if guess is None:
        print("You exited the game. Goodbye!")
        return

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()  # Empty line for better layout
        guess = get_valid_guess("Enter a new guess (or press Enter to quit): ")
        if guess is None:
            print("You exited the game. Goodbye!")
            return

    print(f"Congrats! The number was: {secret_number}")

def get_valid_guess(prompt):
    while True:
        user_input = input(prompt) 
        if user_input.strip() == "":  # User pressed Enter without typing a number
            return None  # Exit the game by returning None
        elif user_input.strip().isdigit():  # Check if the input is a valid number
            return int(user_input)  # Return the number as an integer
        else:
            print("Please enter a valid number!")  # Inform user if the input is not valid

if __name__ == '__main__':
    main()
