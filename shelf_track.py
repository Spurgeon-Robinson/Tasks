# This program is a bookkeeping application for tracking items on shelves.
# It allows users to add, update information about items,
# remove items, and view the current inventory.
from create_book_database import get_sql_cursor

# Create database and get cursor
cursor = get_sql_cursor()


def add_book(book_id, title, author_id, author_name, author_country, quantity):
    """Adds a new book to the the database, and saves the changes, to both
       'insert_book_values.sql' and 'insert_author_values.sql'."""
    insert_str = """INSERT INTO Books (book_id, book_title, authorID, quantity)
                    VALUES (?, ?, ?, ?);"""
    cursor.execute(insert_str, (book_id, title, author_id, quantity))
    cursor.connection.commit()

    # Add author information
    insert_author_str = """INSERT INTO Authors (ID, author_name, country)
                           VALUES (?, ?, ?);"""
    cursor.execute(insert_author_str, (author_id, author_name, author_country))
    cursor.connection.commit()


def update_book(
        book_id, new_title, new_author_id, new_author_name,
        new_country, new_quantity
        ):
    """Allows user to update book information,
       Showing current information first, then updating to new values,
       allowing the user to change the title, author ID,
       author name, quantity, and country."""
    update_book_str = """UPDATE Books
                         SET book_title = ?, authorID = ?, quantity = ?
                         WHERE book_id = ?;"""
    cursor.execute(update_book_str,
                   (new_title, new_author_id, new_quantity, book_id))

    update_author_str = """UPDATE Authors
                           SET author_name = ?, country = ?
                           WHERE ID = ?;"""
    cursor.execute(update_author_str,
                   (new_author_name, new_country, new_author_id))
    cursor.connection.commit()
    print("Book information updated successfully.")


def remove_book(book_id):
    """Removes a book from the inventory, if it exists."""
    delete_str = "DELETE FROM Books WHERE book_id = ?;"
    cursor.execute(delete_str, (book_id,))
    # Print confirmation message
    if cursor.rowcount > 0:
        print(f"Book ID {book_id} removed successfully.")
    else:
        print(f"Book ID {book_id} not found in the database.")
        cursor.connection.rollback()


def search_book_by_title(title):
    """Searches for books by title."""
    search_str = "SELECT * FROM Books WHERE book_title LIKE ?;"
    cursor.execute(search_str, ('%' + title + '%',))
    results = cursor.fetchall()
    print("\nSearch results:\n")
    if results:
        for row in results:
            print("-" * 50)
            print(f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor ID:\
 {row[2]}\nQuantity: {row[3]}")
    else:
        print("No books found with that title.")


def view_all_details():
    """Gets details from 'books' table, and 'Authors' table
       and displays them."""
    cursor.execute("""
        SELECT Books.book_title, Authors.author_name, Authors.country
        FROM Books
        JOIN Authors ON Books.authorID = Authors.ID;
    """)
    results = cursor.fetchall()
    print("\nBook details:\n")
    if results:
        for row in results:
            print("-" * 50)
            print(f"Title: {row[0]}\nAuthor Name:\
 {row[1]}\nAuthor Country: {row[2]}")
    else:
        print("No books found.")


# Main loop for user interaction
while True:
    user_input = int(
        input(
            """\nChoose an option:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search book
    5. View details of all books
    0. Exit
    """
        )
    )
    # Process user input
    if user_input == 1:
        choice = input("Enter '-1' to cancel or '1' to continue: ")
        # if user wants to cancel, return to main menue
        if choice == "-1":
            continue
        elif choice == "1":
            # Validate user input for adding a book
            book_id = input("Enter book ID: ")
            while not book_id.isdigit() or len(book_id) != 4:
                print("Invalid book ID. Please enter a 4-digit ID.")
                book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            while not author_id.isdigit() or len(author_id) != 4:
                print("Invalid author ID. Please enter a 4-digit ID.")
                author_id = input("Enter author ID: ")
            author_name = input("Enter author name: ")
            author_country = input("Enter author country: ")
            quantity = input("Enter quantity: ")
            while not quantity.isdigit():
                print("Invalid quantity. Please enter a valid number.")
                quantity = input("Enter quantity: ")
            # Check if all required fields are filled
            if not all([book_id, title, author_id,
                        author_name, author_country, quantity]):
                print("All fields are required.")
                continue
            # Check if quantity is a valid number
            if not quantity.isdigit():
                print("Invalid quantity. Please enter a valid number.")
                continue
            add_book(
                book_id,
                title,
                author_id,
                author_name,
                author_country,
                int(quantity)
            )

    elif user_input == 2:
        choice = input("'-1' to cancel or '1' to continue:")
        if choice == "-1":
            continue
        elif choice == "1":
            # Get book ID
            book_id = input("Enter book ID to update: ")
            # If book ID not found, notify user and return to main menu
            cursor.execute(
                "SELECT * FROM Books WHERE book_id = ?;", (book_id,)
                )
            if cursor.fetchone() is None:
                print("Book ID not found.")
                continue
            # Fetch and display current book information,
            # from 'books' and 'Authors' tables
            cursor.execute(
                "SELECT * FROM Books WHERE book_id = ?;", (book_id,)
            )
            current_book = cursor.fetchone()
            cursor.execute(
                "SELECT * FROM Authors WHERE ID = (SELECT authorID\
 FROM Books WHERE book_id = ?);", (book_id,)
            )
            current_author = cursor.fetchone()
            # Display current book information
            if current_book and current_author:
                print("Current book information:")
                print(f"Title: {current_book[1]}")
                print(f"Author Name: {current_author[1]}")
                print(f"Author Country: {current_author[2]}")
                print(f"Quantity: {current_book[3]}")
            else:
                print("Book not found.")
            # Allow user to choose which fields to update
            # Validate the new inputs
            new_title = input(
                "Enter new title (leave blank to keep current): "
                )
            new_author_id = input(
                    "Enter new author ID (leave blank to keep current): "
                )
            while new_author_id and (
                    not new_author_id.isdigit() or len(new_author_id) != 4):
                print("Invalid author ID. Please enter a 4-digit ID.")
                new_author_id = input(
                    "Enter new author ID (leave blank to keep current): "
                )
            new_quantity = input(
                "Enter new quantity (leave blank to keep current): "
                )
            while new_quantity and not new_quantity.isdigit():
                print("Invalid quantity. Please enter a valid number.")
                new_quantity = input(
                    "Enter new quantity (leave blank to keep current): "
                )
            new_author_name = input(
                "Enter new author name (leave blank to keep current): "
                )
            new_country = input(
                "Enter new author country (leave blank to keep current): "
                )
            # Set new values, keeping current if input is blank
            if not new_title:
                new_title = current_book[1]
            if not new_author_id:
                new_author_id = current_book[2]
            if not new_quantity:
                new_quantity = current_book[3]
            else:
                new_quantity = int(new_quantity)
            if not new_author_name:
                new_author_name = current_author[1]
            if not new_country:
                new_country = current_author[2]
            # Update the book and author information in the database
            cursor.execute("""
                UPDATE Books
                SET book_title = ?, authorID = ?, quantity = ?
                WHERE book_id = ?;
            """, (new_title, new_author_id, new_quantity, book_id))
            cursor.execute("""
                UPDATE Authors
                SET author_name = ?, country = ?
                WHERE ID = (SELECT authorID FROM Books WHERE book_id = ?);
            """, (new_author_name, new_country, book_id))
            cursor.connection.commit()
            print("Book information updated successfully.")

    elif user_input == 3:
        choice = input("'-1' to cancel or '1' to continue: ")
        if choice == "-1":
            continue
        elif choice == "1":
            remove_book(input("Enter book ID to remove: "))
            cursor.connection.commit()

    elif user_input == 4:
        choice = input("'-1' to cancel or '1' to continue: ")
        if choice == "-1":
            continue
        elif choice == "1":
            search_book_by_title(input("Enter book title to search: "))
    elif user_input == 5:
        view_all_details()

    elif user_input == 0:
        print("Exiting program.")
        break
    # Invalid option handlin
    else:
        print("Invalid option. Please try again.")
