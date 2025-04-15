def main():
    # Dictionary with fruit names and their prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0  

    # Loop through each fruit
    for fruit_name in fruits:
        while True:
            amount_input = input(f"How many ({fruit_name}) do you want?: ")
            if amount_input.strip() == "":
                print("Please enter a number (you left it blank).")
                continue
            try:
                amount = int(amount_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Calculate cost and add to total
        total_cost += amount * fruits[fruit_name]

    # Show final total cost
    print(f"\nYour total is ${total_cost}")


if __name__ == '__main__':
    main()
