# This program cyphers input text by shifting alphabetical
# characters by 15 positions.
# Non-alphabetical characters remain unchanged.
# The program continues to prompt the user for input until they choose to exit.

def cypher(text):
    '''Cypher the input text using a shift of 15
       for alphabetical characters.'''
    result = ""
    # Iterate through each character in the input text using a for loop
    for char in text:
        if char.isalpha():
            shift = 15
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


def main():
    '''Loop the main function, so the user can try again.'''
    while True:
        user_input = input("Enter text to cypher (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        cyphered_text = cypher(user_input)
        print("Cyphered text:", cyphered_text)


if __name__ == "__main__":
    main()
