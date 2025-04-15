def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty dictionary for storing phonebook entries.





def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":  # If the user enters an empty string, stop the lookup process.
            break
        if name not in phonebook:  # If the name is not in the phonebook.
            print(f"{name} is not in the phonebook.")
        else:  # If the name is found in the phonebook.
            print(f"{name}'s number is {phonebook[name]}.")


def main():
    phonebook = read_phone_numbers()  # Get the phonebook entries from the user.
    print_phonebook(phonebook)  # Print out the phonebook.
    lookup_numbers(phonebook)  # Allow the user to lookup phone numbers.


# Python boilerplate.
if __name__ == '__main__':
    main()
