# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# Pythagorean Theorem Kya Hai?
# Agar ek right-angled triangle ho, jisme do perpendicular sides (AB aur AC) di gayi hon, to hypotenuse (BC) ko calculate karne ka formula yeh hai:

import math

def calculate_hyp(side1, side2):

    return math.sqrt(side1**2 + side2**2)

def main():
    print("Right Triangle Hypotenuse Calculator")
    print("-----------------------------------")
    
    try:
        # Get user input with validation
        ab = float(input("Enter the length of side AB: "))
        ac = float(input("Enter the length of side AC: "))
        
        # Validate inputs are positive
        if ab <= 0 or ac <= 0:
            # raise ValueError ka use kiya gaya hai jo ek error message show karega.
            raise ValueError("Side lengths must be positive numbers")
        
        # Calculate and display result
        hypotenuse = calculate_hyp(ab, ac)
        print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse:.2f}")
        
    except ValueError as e:
        print(f"\nError: {e}. Please enter valid positive numbers.")

if __name__ == '__main__':
    main()