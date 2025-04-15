# This problem is about creating a **Planetary Weight Calculator** in Python. The idea is to help users find out how much they would weigh on other planets based on the gravity differences. First, the program should ask for the user's weight on Earth and calculate how much they'd weigh on **Mars**,
# where gravity is 37.8% of Earth’s. In the second part, the program expands to support **all planets** in our solar system,
# each with a different gravity percentage. The user enters their Earth weight and chooses a planet, and the program calculates and displays the weight on that planet, rounded to two decimal places. The logic involves simple input handling, condition checking, and basic math using gravity constants.

# Milestone #2: Complete Planetary Weight Calculator

def main():
    # Gravity factors relative to Earth for each planet
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Get user input
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    # Lookup gravity factor for selected planet
    gravity = gravity_factors[planet]

    # Calculate and round weight
    planet_weight = round(earth_weight * gravity, 2)

    # Print result
    print(f"The equivalent weight on {planet}: {planet_weight}")

if __name__ == "__main__":
    main()
