# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_die(sides=6):
    """Simulate rolling a single die with given number of sides."""
    return random.randint(1, sides)

def main():
    print("Dice Rolling Simulation")
    print("----------------------")
    
    # Roll two standard 6-sided dice
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2
    
    # Display results with formatting
    print(f"\nDie 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}\n")
    
    # Optional: Add ASCII art of dice faces
    dice_faces = {
        1: "[ • ]",
        2: "[•  •]",
        3: "[• • •]",
        4: "[• •\n• •]",
        5: "[• • •\n • • ]",
        6: "[• • •\n• • •]"
    }
    print("Visualization:")
    print(f"Die 1: {dice_faces[die1]}")
    print(f"Die 2: {dice_faces[die2]}")

if __name__ == '__main__':
    main()