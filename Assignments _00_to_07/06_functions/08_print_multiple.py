def print_multiple(message: str, repeats: int):

    for i in range(repeats):
        print(message)

def main():
    
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Function ko call kar ke message ko repeat print karwana hai
    print_multiple(message, repeats)

# Program ka start point
if __name__ == '__main__':
    main()
