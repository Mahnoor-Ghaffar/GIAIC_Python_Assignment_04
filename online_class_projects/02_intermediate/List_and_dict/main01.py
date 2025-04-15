def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        old = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old}' with '{new_value}'."
    else:
        return "Index out of range!"

def slice_list(my_list, start, end):
    try:
        sliced = my_list[start:end]
        return f"Sliced list: {sliced}"
    except:
        return "Invalid slice indices!"

def game():
    # Initial list
    my_list = ['cat', 'dog', 'parrot', 'hamster', 'fish']
    
    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation: access / modify / slice / quit")
        choice = input("Your choice: ").strip().lower()

        if choice == 'access':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == 'modify':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == 'slice':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == 'quit':
            print("Thanks for playing!")
            break

        else:
            print("Invalid option. Try again!")

# Run the game
game()
