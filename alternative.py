user_string = input("Please enter a sentence: ")  # Input from the user
# Makes the alternating characters uppercase and lowercase
alternate_uppercase = "".join(
    char.upper() if i % 2 == 0 else char.lower()
    for i, char in enumerate(user_string)
)
# Prints the modified string with alternating uppercase and lowercase letters
print(alternate_uppercase)
# Makes the words in the sentence alternate between uppercase and lowercase
alternative_word = " ".join(
    word.upper() if i % 2 == 0 else word.lower()
    for i, word in enumerate(user_string.split())
)
# Prints the modified sentence with alternating uppercase and lowercase words
print(alternative_word)
