"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    global list_of_emails
    email_1 = {
        "email_address": "alice@example.com",
        "subject_line": "Meeting Reminder",
        "email_content": "Don't forget about the meeting at 10 AM tomorrow.",
        "has_been_read": False,  # Initially, all emails are unread.
    }
    email_2 = {
        "email_address": "james@example.com",
        "subject_line": "Project Update",
        "email_content": "The project is on track for completion next week.",
        "has_been_read": False,  # Initially, all emails are unread.
    }
    email_3 = {
        "email_address": "jane@example.com",
        "subject_line": "Newsletter",
        "email_content": "Welcome to our monthly newsletter!",
        "has_been_read": False,  # Initially, all emails are unread.
    }
    email_4 = {
        "email_address": "jade@example.com",
        "subject_line": "Party Invitation",
        "email_content": "You're invited to my birthday party this Saturday!",
        "has_been_read": False,  # Initially, all emails are unread.
    }
    list_of_emails = [email_1, email_2, email_3, email_4]
    pass


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index, email in enumerate(list_of_emails):
        print(f"{index}: {email['subject_line']}")
    pass


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    # Using a try-except block to handle invalid index input
    try:
        email = list_of_emails[index]
        print(f"From: {email['email_address']}")
        print(f"Subject: {email['subject_line']}")
        print(f"Content: {email['email_content']}")
        email['has_been_read'] = True
    except IndexError:
        print("Invalid index. Please try again.")
    pass


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    print("Unread Emails:")
    # Using a for loop with enumerate to get index and email
    for index, email in enumerate(list_of_emails):
        if not email['has_been_read']:
            print(f"{index}: {email['subject_line']}")
    pass


# --- Email Program --- #

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
list_of_emails = []

# Fill in the logic for the various menu operations.

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        # Call the function to list all emails with their index numbers
        list_emails()
        # Prompt the user to select an email by its index number
        email_index = int(
            input("Enter the index number of the email to read: ")
        )
        # Call the function to read the selected email
        read_email(email_index)
        pass

    elif user_choice == 2:
        # Add logic here to view unread emails
        # Call the function to
        view_unread_emails()
        # If there are no unread emails, inform the user
        if not any(not email['has_been_read'] for email in list_of_emails):
            print("No unread emails.")
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Goodbye!")
        break

    else:
        # Handle invalid input
        print("Oops - incorrect input.")
