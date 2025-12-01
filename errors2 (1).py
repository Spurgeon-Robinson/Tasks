# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # No quotation marks around Lion, added quotation marks to make it a string
animal_type = "Cub"
number_of_teeth = 16

full_spec = "This is a " + str(animal) + "." " It is a " \
 + str(animal_type) + " and it has " + str(number_of_teeth) + " teeth." # Incorrect formatting, added str() to convert variables to string

print(full_spec) # couldn't print because there were no parentheses, added parentheses to print function
