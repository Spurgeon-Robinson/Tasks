# This code is a list of frinds and their ages
friends_names = ["Bob", "Sett", "Linus"]
# Slicing the list to get the first element
print(friends_names[0:1])
# Slicing the list to get the third element
print(friends_names[2:3])
# Printing the length of the list
print("The lenth of the list is:", len(friends_names))
# List of ages corresponding to the friends
friends_ages = [19, 20, 21]
# Printing each friend's name and age using a loop
for i in range(len(friends_names)):
    print(friends_names[i], "is", friends_ages[i], "years old.")
