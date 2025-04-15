def get_user_numbers():

    # """
    # Get a list of numbers from the user.
    # Stops when the user enters a blank line.
    # """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

# """
#     Count how many times each number appears in the list.
#     Returns a dictionary with number as key and count as value.
# """
def count_numbers(number_list):
    
    number_counts = {}
    for num in number_list:
        if num not in number_counts:
            number_counts[num] = 1
        else:
            number_counts[num] += 1
    return number_counts


# """
#     Print how many times each number appears.
# """
def print_counts(number_counts):
    
    for num in number_counts:
        print(f"{num} appears {number_counts[num]} times.")


#  Main function to run the program.
def main():
   
    user_numbers = get_user_numbers()
    number_counts = count_numbers(user_numbers)
    print_counts(number_counts)

if __name__ == '__main__':
    main()
