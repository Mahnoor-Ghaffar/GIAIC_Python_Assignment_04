# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!
# " (the blank should be filled in with the user-inputted animal, of course).


# ----------Solution
def main():
    # Prompt the user to enter their favorite animal
    animal = input("What's your favorite animal? ")

    # Print the response with the user's input
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    main()