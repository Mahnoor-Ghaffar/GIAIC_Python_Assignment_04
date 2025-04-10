# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2

# ---------------Solution

# Speed of light constant
C = 299792458  


def main():

    # User input
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Energy calculation
    energy_in_joules = mass_in_kg * (C ** 2)

    # Results ko print karna
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")  # Mass dikhana
    print(f"C = {C} m/s")  # Speed of light dikhana
    print(f"{energy_in_joules} joules of energy!")  # Energy result


if __name__ == '__main__':
    main()