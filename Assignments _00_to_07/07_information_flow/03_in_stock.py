def main():
    # Step 1: User se fruit ka naam lena
    fruit: str = input("Enter a fruit: ")

    # Step 2: Check karna stock mein kitna hai
    stock = num_in_stock(fruit)

    # Step 3: Agar 0 hai toh "not in stock" print karna
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        # Step 4: Agar 0 se zyada hai toh quantity print karo
        print("This fruit is in stock! Here is how many:")
        print(stock)

# Helper Function
def num_in_stock(fruit):
    """
    Yeh function check karta hai ke kis fruit ka kitna stock hai.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # Agar koi aur fruit diya gaya ho jo stock mein nahi hai
        return 0

# Program run start hota hai yahan se
if __name__ == '__main__':
    main()
