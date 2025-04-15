import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for _ in range(N_NUMBERS):
        value = random.radiant(N_NUMBERS)
        print(value, end=' ')

if __name__ == '__main__':
    main()