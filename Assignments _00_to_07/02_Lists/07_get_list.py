def main():
    lst = []  # Create an empty list 

    val = input("Enter a value: ") 
    while val: 
        lst.append(val)  
        val = input("Enter a value: ")  

    print("Here's the list:", lst)


# This provided line is required to call the main() function when this script is run
if __name__ == '__main__':
    main()
