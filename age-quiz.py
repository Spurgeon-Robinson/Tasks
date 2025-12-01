#Ask for age
age = int(input("How old are you? "))
#add if statment, figure out the order of if statments so it all works properly
if age > 100:
    print("Sorry, you're dead.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 45:
    print("You're over the hill.")
else :
    print("Age is but a number.")