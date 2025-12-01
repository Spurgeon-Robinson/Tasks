# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # didn't have any parentheses
print() # didn't have any parentheses, didn't add new line correctly

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # cahnged "24 years old" to "24" to avoid casting issues, changed "==" to "="  
age = int(age_Str)
print("I'm " + str(age) + " years old.") # corrected "+ age +" to "+ str(age) + " to avoid type error, added space after "I'm" and before "years old."

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # removed quotation marks to make it an integer
total_years = age + years_from_now

print("The total number of years: " + str(total_years)) # didn't have any parentheses, incorrect variable name "answer_years" changed to "total_years" changed variable to string with "str(total_years)"

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 + 6  # incorrect variable name "total" changed to "total_years", and added "+ 6" to account for the additional 6 months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old.") # no parentheses, changed "+ total_months +" to "+ str(total_months) + " to avoid type error
# HINT, 330 months is the correct answer
