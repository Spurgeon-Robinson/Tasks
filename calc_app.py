# This program is a simple calculator application.
# It performs simple arithmetic operations,
# And stores the results in a file named equations.txt,
# allowing users to review their calculations later.

import os


def calculate():
    """Main function to run the calculator.
       It prompts the user for input, performs calculations,
       and saves the results to a file."""
    print("\nWelcome to the Simple Calculator!")
    print("Enter your calculations in the format: number1 operator number2")
    print("Operators supported: +, -, *, /")
    # A loop to continuously accept user input
    while True:
        # Prompting user for input
        user_equation = input(
            "Type 'exit' to quit the calculator.\n"
            "Type 'view' to see the logged equations. \n"
            "Enter your calculation: "
            )
        # Handling special commands
        if user_equation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        # If the user wants to view logged equations
        if user_equation.lower() == 'view':
            if os.path.exists("equations.txt"):
                with open("equations.txt", "r", encoding="utf-8") as file:
                    print("Equations Log:\n")
                    print(file.read())
            # If the file does not exist or is empty
            else:
                print("No equations logged yet.")
        # Processing the user input for calculations
        try:
            parts = user_equation.split()
            # Ensure the input is in the correct format,
            # If the input is empty, prompt the user again
            if not parts:
                print("\nNo input provided. Please enter a calculation.\n")
                continue
            # Skips this error if the input is 'veiw'
            if parts[0].lower() == 'view':
                continue
            # Checking if the input has exactly three parts
            if len(parts) != 3:
                print(
                    "\nInvalid input format."
                    " Please use: number1 operator number2\n"
                    )
                continue
            # Extracting numbers and operator
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            # Performing the calculation based on the operator
            # Using if-elif to determine the operation
            # Handling addition, subtraction, multiplication, and division
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Handling division by zero
                if num2 == 0:
                    print("\nError: Division by zero is not allowed.\n")
                    continue
                result = num1 / num2
            # If the operator is not recognized
            else:
                print("\nInvalid operator. Supported operators: +, -, *, /\n")
                continue
            # Displaying the result to the user
            print("\n"f"Result: {result}\n")
            # Saving the equation and result to the file
            save_equation(user_equation, result)
        # Handling exceptions for invalid input formats
        except ValueError:
            print("\nInvalid number format. Please enter a valid input.\n")


def save_equation(equation, result):
    """Saves the equation and its result to the equations.txt file."""
    with open("equations.txt", "a", encoding="utf-8") as file:
        file.write(f"{equation} = {result}\n")


def main():
    """Main function to initialize the calculator application."""
    # Check if the equations.txt file exists, if not create it
    if not os.path.exists("equations.txt"):
        with open("equations.txt", "w", encoding="utf-8") as file:
            file.write("Equations Log:\n")


calculate()
