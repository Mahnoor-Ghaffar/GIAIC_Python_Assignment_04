import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "⚠️ You must select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    response = input(prompt + " (y/n): ").strip().lower()
    return response == 'y'

def main():
    print("🔐 Advanced Password Generator 🔐\n")

    try:
        count = int(input("🔢 Number of passwords to generate: "))
        length = int(input("🔠 Length of each password: "))

        print("\nSelect character types to include:")
        use_uppercase = get_yes_no_input("Include UPPERCASE letters?")
        use_lowercase = get_yes_no_input("Include lowercase letters?")
        use_digits = get_yes_no_input("Include numbers?")
        use_symbols = get_yes_no_input("Include symbols (!@#...)?")

        print("\n🎯 Generated Passwords:\n" + "-"*30)

        for i in range(count):
            pwd = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print(f"{i+1}. {pwd}")

    except ValueError:
        print("❌ Please enter valid numeric inputs!")

if __name__ == "__main__":
    main()
