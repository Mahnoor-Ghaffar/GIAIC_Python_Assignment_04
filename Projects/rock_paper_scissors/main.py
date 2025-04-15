> Show both user and computer choices with full names (rock/paper/scissors).

> Play multiple rounds (loop until user quits).

> Keep score tracking for both user and computer.

> Validate user input (no crash on wrong input).

> Clean output formatting for better UX.

import random

def get_full_name(short_choice):
    return {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}.get(short_choice, 'Invalid')

def is_win(player, opponent):
    # Returns True if player beats opponent
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play_round():
    user = input("Choose: 'r' for Rock, 'p' for Paper, 's' for Scissors (or 'q' to quit): ").lower()
    if user == 'q':
        return 'quit', None

    if user not in ['r', 'p', 's']:
        print("❌ Invalid input. Please try again.")
        return None, None

    computer = random.choice(['r', 'p', 's'])
    print(f"\n🧍 You chose: {get_full_name(user)}")
    print(f"🤖 Computer chose: {get_full_name(computer)}")

    if user == computer:
        print("⚖️ It's a tie!")
        return 'tie', None
    elif is_win(user, computer):
        print("✅ You won this round!")
        return 'win', 'user'
    else:
        print("❌ You lost this round.")
        return 'loss', 'computer'

def game():
    user_score = 0
    computer_score = 0
    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    print("-----------------------------------------")

    while True:
        result, winner = play_round()

        if result == 'quit':
            break
        elif result is None:
            continue
        elif winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"🏆 Score => You: {user_score} | Computer: {computer_score}\n")

    print("\n🚪 Game Over!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 Congratulations! You beat the computer!")
    elif user_score < computer_score:
        print("💻 The computer wins this time. Better luck next time!")
    else:
        print("⚖️ It's a draw overall!")

if __name__ == "__main__":
    game()
