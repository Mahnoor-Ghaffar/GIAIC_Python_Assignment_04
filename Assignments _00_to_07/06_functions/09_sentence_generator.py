def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
       
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # Agar user ne 1 dia, matlab yeh verb hai
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # Agar user ne 2 dia, matlab yeh adjective hai
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # Agar number 0, 1, ya 2 nahi hai, toh error 
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    # User se word lo
    word: str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    
    # Part of speech number lo (0, 1, 2)
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Sentence generate karne wala function call karo
    make_sentence(word, part_of_speech)

# Python program start yahan se hota hai
if __name__ == '__main__':
    main()
