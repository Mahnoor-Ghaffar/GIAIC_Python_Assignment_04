"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

# Import the random library to simulate random dice rolls
import random

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    # Optional: Set a seed for reproducibility (useful for debugging)
    # random.seed(1)
    
    # Roll two dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total
    total: int = die1 + die2
    
    # Print results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Call the main function
if __name__ == '__main__':
    main()
