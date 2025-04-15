#  Python Mad Libs game
# -------------------------
# Asks the user to input an adjective, two verbs, and the name of a famous person.

# Inserts those words into a funny sentence (called a madlib).

# Prints the final sentence with the user’s inputs.

# Mad Libs Game 🎉

# Get inputs from the user
adjective = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
famous_person = input("Enter the name of a famous person: ")

# Create the madlib using an f-string
madlib = (
    f"Computer programming is so {adjective}! "
    f"It makes me so excited all the time because I love to {verb1}. "
    f"Stay hydrated and {verb2} like you are {famous_person}!"
)

# Print the final madlib
print("\nHere is your Mad Lib:\n")
print(madlib)
