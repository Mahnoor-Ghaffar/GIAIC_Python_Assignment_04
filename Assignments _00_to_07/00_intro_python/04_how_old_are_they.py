# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful!



# -------------------Solution

def main():
    Anton : init = 21
    Beth : init = 6 + Anton
    Chen : init = 20 + Beth
    Drew : init = Chen + Anton
    Ethan : init = Chen

    # Results
    print("Anton is", Anton)
    print("Beth is", Beth)
    print("Chen is", Chen)
    print("Drew is", Drew)
    print("Ethan is", Ethan)

if __name__ == '__main__':
    main()