# Stores incorrect names in "incorrect_names"
incorrect_names = {}
# Asks the user for name input
user_name = input("Enter your name: ")
# continues to ask for names until "john" is entered
while user_name.lower() != "john":
    # Adds the name to the dictionary or increments its count if it already exists
    if user_name.lower() in incorrect_names:
        incorrect_names[user_name.lower()] += 1
    else:
        incorrect_names[user_name.lower()] = 1
    user_name = input("Enter your name: ")
# When "john" is entered, the loop ends and the dictionary is printed
# Uses the keys() method to get only the names
print(list(incorrect_names.keys()))
