import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print("\nThink of a number between 1 and", x, "and the computer will try to guess it!")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  
        print(f"\n🤖 Computer guesses: {guess}")  # Show the guess
        feedback = input("Is the guess too High (H), too Low (L), or Correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter only H, L, or C.")

    print(f"\n🎉 Yay! The computer guessed your number: {guess} correctly!")

if __name__ == "__main__":
    computer_guess(10)
