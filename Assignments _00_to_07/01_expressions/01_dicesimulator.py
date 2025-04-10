# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

NUM_SIDES = 6

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2 :int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"Rolled: {die1} and {die2} (total: {total})")

def main():

    # die1 variable ki value 10 set ki gayi hai.Phir usko print kiya gaya hai.
    die1: int = 10
    print(f"\nStarting main() - die1 value: {die1}")
    
    # Yeh for loop 3 dafa roll_dice() function ko call karega.
    print("\nRolling dice three times:")
    for _ in range(3):
        roll_dice()
    
    print(f"\nAfter rolling - die1 value in main() remains: {die1}")
    print("This shows the die1 in main() is separate from die1 in roll_dice()")

if __name__ == '__main__':
    main()