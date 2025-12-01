
# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return (f"Shoe(country: {self.country}, code: {self.code}"
                f" Product: {self.product}, cost: {self.cost}"
                f", quantity: {self.quantity})")


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    One line in this file represents
    data to create one object of shoes.
    You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                country, code, product, cost, quantity = line.strip(
                ).split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: The file inventory.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("")
    print("Capture New Shoe")
    print("")
    # Get country from user
    country = input("Enter 'm' for main menu, or enter country: ")
    # Return to main menu if 'm' is entered
    if country.lower() == 'm':
        return
    # Validate country input
    while not country.isalpha():
        country = input("Invalid input. Country must contain"
                        " only letters. Please re-enter country: ")
    # Get shoe code from user
    code = input("Enter 'm' for main menu, or enter shoe code: ")
    # Return to main menu if 'm' is entered
    if code.lower() == 'm':
        return
    # Validate code input
    while not code.isalnum():
        code = input("Invalid input. Code must be alphanumeric."
                     " Please re-enter shoe code: ")
    # Get product name from user
    product = input("Enter 'm' for main menu, or enter product name: ")
    # Return to main menu if 'm' is entered
    if product.lower() == 'm':
        return
    # Skip validation for product name (can contain spaces and letters)
    # Get cost from user
    cost = input("Enter 'm' for main menu, or enter cost: ")
    # Return to main menu if 'm' is entered
    if cost.lower() == 'm':
        return
    # Validate cost input
    while not cost.replace('.', '', 1).isdigit() or float(cost) < 0:
        cost = input("Invalid input. Cost must be a number 0"
                     " or greater. Please re-enter cost: ")
    # Get quantity from user
    quantity = input("Enter 'm' for main menu, or enter quantity: ")
    # Return to main menu if 'm' is entered
    if quantity.lower() == 'm':
        return
    # Validate quantity input
    while not quantity.isdigit() or int(quantity) < 0:
        quantity = input("Invalid input. Quantity must be a"
                         " number 0 or greater. Please re-enter quantity: ")
    # Create new Shoe object and add to shoe_list
    shoe = Shoe(country, code, product, float(cost), int(quantity))
    shoe_list.append(shoe)
    # Write this new shoe to the inventory.txt file
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    print("")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print("")
    print(f"Lowest quantity shoe: {lowest_shoe}")
    restock_quantity = input("Enter quantity to add, or '-1' for main menu: ")
    if restock_quantity == '-1':
        return
    # Validate restock quantity input
    while not restock_quantity.isdigit() or int(restock_quantity) < 0:
        restock_quantity = input(
            "Invalid input. Quantity must be a number 0"
            " or greater. Please re-enter quantity to add: "
        )
    # Update the quantity of the lowest shoe
    lowest_shoe.quantity += int(restock_quantity)
    print(f"Updated shoe: {lowest_shoe}")
    # Update the inventory.txt file
    with open("inventory.txt", "w") as file:
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},"
                       f"{shoe.cost},{shoe.quantity}\n")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search_code = input("Enter shoe code to search, or 'm' for main menu: ")
    if search_code == 'm':
        return
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("")
            print(shoe)
            return
    else:
        print("Shoe code not found.")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print("")
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Total value for {shoe.product}"
              f" (Code: {shoe.code}): ${value:.2f}")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print("")
    print(f"Shoe with highest quantity (for sale): {highest_shoe}")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


def main():
    read_shoes_data()
    # Infinite loop for menu
    while True:
        # Display menu options
        print("\nShoe Inventory Management System")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Re-stock Shoes")
        print("4. Search Shoe")
        print("5. Value per Item")
        print("6. Highest Quantity Shoe")
        print("7. Exit")
        choice = input("Enter your choice: ")
        # Execute corresponding function based on user choice
        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Exiting the program.")
            break
        # Handle invalid choices
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
