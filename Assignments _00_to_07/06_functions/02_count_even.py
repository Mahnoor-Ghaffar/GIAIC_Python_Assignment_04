def count_even(lst):
   
    count = 0  
    for num in lst:
        if num % 2 == 0:  
            count += 1
    print(count)  


def get_list_of_ints():
   
    lst = []  # Create empty list
    user_input = input("Enter an integer or press enter to stop: ")  # First prompt
    while user_input != "":
        lst.append(int(user_input))  # Convert to int and add to list
        user_input = input("Enter an integer or press enter to stop: ")  # Next prompt
    return lst  


def main():
    # calling functions
    lst = get_list_of_ints()  
    count_even(lst)  



if __name__ == '__main__':
    main()
