# Simple logic error
age = input("How old are you? :")
double_age = age * 2  # This line has a logic error; it should convert age to an integer before multiplying
print("Your age doubled is: " + double_age)  # This line has a logic error; it should convert duble_age to an integer before printing
# To fix the logic error, we need to convert the input age to an integer before performing the multiplication and also convert the result back to a string for printing.
