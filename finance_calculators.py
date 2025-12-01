import math
# Finance Calculators
print("Investment - to calculate the amount of interest you'll earn on your\
 investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
# ask for choice between investment and bond
finance_choice = input("Enter either “investment” or “bond” from the menu \
above to proceed: ")
# Add if statment to check if the user input is investment or bond
if finance_choice.lower() == "investment":
    # Ask user for input for investment calculation
    deposit_amount = float(input("Enter the amount of deposit: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years_of_investment = int(input("Enter the number of years: "))
    interest = input("Is your interest simple or compound? ")
    # Ask use if interest is simple or compound
    if interest.lower() == "simple":
        # Calulate based on user input
        total_amount = deposit_amount * \
            (1 + interest_rate / 100 * years_of_investment)
        print(f"Total amount is {total_amount}")
    elif interest.lower() == "compound":
        total_amount = deposit_amount * math.pow \

        ((1+interest_rate / 100), years_of_investment)
        print(f"Total amount is {total_amount}")
    # print invalid if the user input is not simple or compound
    else:
        print("Invalid interest type. Please enter either “simple”\
 or “compound”.")
    # Add elif statemtent if user input is bond
elif finance_choice.lower() == "bond":
    # Ask user for input for bond calculation
    present_value = float(input("What is the present value of the house? "))
    house_interest_rate = float(input("What is the interest rate? "))
    mouths_of_payment = int(input("How many mouths of payment? "))
    # Calculate monthly repayment based on user input
    repayment = (house_interest_rate / 100 / 12 * present_value) / \
        (1 - (1 + house_interest_rate / 100 / 12)**(-mouths_of_payment))
    print(f"Your mounthly repayment is : {repayment}")
    # print invalid if user input was not investment or bondelse:
else:
    print("Invalid choice. Please enter either “investment” or “bond”.")
