import random

NUM_ROUNDS = 5  # You can change this value for more or fewer rounds

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Milestone #5: Points system

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")

        # Extension #1: Get guess with input validation and quit option
        guess = get_user_guess("Do you think your number is higher or lower than the computer's?: ")

        # Milestone #3: Game logic
        if user_number == computer_number:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        elif guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")  # Milestone #5

    # Extension #2: Conditional ending messages
    print("Thanks for playing!")
    print(f"Final Score: {score} out of {NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Extension #1: Input validation + Exit on Enter
def get_user_guess(prompt):
    while True:
        guess = input(prompt).strip().lower()
        if guess == "":
            print("You exited the game. Goodbye!")
            exit()
        elif guess in ("higher", "lower"):
            return guess
        else:
            print("Please enter either higher or lower.")

if __name__ == "__main__":
    main()
