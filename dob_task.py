contents = " "
# This code reads the file DOB.txt and prints the names in a list, then prints the birthdates in a list.
print("Names:")
# opens the file "DOB.txt" in read mode
with open("DOB.txt", "r") as file:
    contents = file.read()
# Prints the names from the file by splitting the lines
for line in contents.splitlines():
    names = line.split()
    if len(names) >= 2:
        print(f"{names[0]} {names[1]}")
print("")
print("Birthdates:")
# Prints the birthdates from the file by splitting the lines
for line in contents.splitlines():
    birthdate = line.split()
    if len(birthdate) >= 3:
        print(" ".join(birthdate[-3:]))
