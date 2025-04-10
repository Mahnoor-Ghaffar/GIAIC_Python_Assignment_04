# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    print("Division with Remainder Calculator")

    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        # Validate divisor is not zero
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")

            # Calculate quotient and remainder
        quotient = dividend // divisor
        remainder = dividend % divisor

        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("\nError: Please enter valid integers only")
    except ZeroDivisionError as e:
        print(f"\nError: {e}")

if __name__ == '__main__':
    main()