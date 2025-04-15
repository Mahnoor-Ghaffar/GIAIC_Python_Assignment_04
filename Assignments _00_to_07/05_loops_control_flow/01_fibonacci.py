# It’s a mathematical sequence where:

# The first two numbers are: 0 and 1

# Every number after that is the sum of the previous two

# Constant for maximum value in the Fibonacci sequence
MAX_TERM_VALUE = 10000

def main():
    curr_term = 0  # Starting with Fib(0)
    next_term = 1  # Then Fib(1)
    
    # Keep printing terms until we reach or cross 10,000
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=' ')  # print on the same line with a space
        term_after_next = curr_term + next_term  # Next Fibonacci number
        curr_term = next_term
        next_term = term_after_next

# This calls main() when we run the script
if __name__ == '__main__':
    main()
