# Define the affirmation you want the user to type
AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    # Take user input
    user_input = input()

    # Keep asking until the user types the affirmation correctly
    while user_input != AFFIRMATION:
        print("Hmmm That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()

    # If user types it correctly
    print("That's right! :)")

if __name__ == '__main__':
    main()
