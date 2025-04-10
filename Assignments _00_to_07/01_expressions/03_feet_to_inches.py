# Converts feet to inches.
# Feet is an American unit of measurement.
# There are 12 inches per foot.
# Foot is the singular, and feet is the plural.


# ------------SOLUTION

INCHES_PER_FOOT = 12

def main():
    # Get input from user for number of feet.
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_PER_FOOT

    # Display the result as a formatted string
    print(f"{feet} feet equals {inches} inches")


if __name__ == '__main__':
    main()