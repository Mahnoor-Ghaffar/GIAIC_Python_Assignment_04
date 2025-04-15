# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12


# The purpose of this function is to take a number as input (for example, 12) 
# and print all of its divisors — that is, all the numbers that divide it evenly (without leaving any remainder).

def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # 1 se num tak loop chalega
        if num % i == 0:  # agar num i se cleanly divide ho jaye
            print(i)

def main():
    num = int(input("Enter a number: "))  # user se input lein
    print_divisors(num)  # function ko call karein

# Neeche wali line program ka start point hai
if __name__ == '__main__':
    main()
