# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


def reg_user():
    '''Add a new user to the user.txt file'''

    # Request input of a new username
    new_username = input(
        "-1 to go back to main menu.\n"
        "New Username: "
        )
    if new_username == '-1':
        return

    # Request input of a new password
    new_password = input(
        "-1 to go back to main menu.\n"
        "New Password: "
        )

    # Request input of password confirmation.
    confirm_password = input(
        "-1 to go back to main menu.\n"
        "Confirm Password: "
        )
    # Check if the new username already exists in the user.txt file.
    if new_username in username_password.keys():
        print("Username already exists. Please choose a different username.")
        return
    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    # Otherwise you present a relevant message.
    else:
        print("Passwords do not match. Please try again.")


def add_task():
    ''' Allow a user to add new task to the task.txt file
        Prompt a user for the following:
        - The username of the person whom the task is assigned to,
        - The title of the task,
        - The description of the task and
        - The due date of the task.'''

    task_username = input(
        "-1 to go back to main menu.\n"
        "Name of person assigned to task: "
    )
    if task_username == '-1':
        return
    # Check if the user exists in the username_password dictionary
    # If not, prompt the user to enter a valid username
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    # Get the title of the task
    task_title = input("Title of task: ")
    # Get the description of the task
    task_description = input("Description of task: ")
    # Get the due date of the task
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break
        # If the date format is incorrect, prompt the user to enter it again
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''

    # Create a new task dictionary
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    # Write the new task to the tasks.txt file
    # Convert the task list to a string format for writing
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    '''Reads the task from task.txt file and prints to the console in the
       format of Output 2 presented in the task pdf
       (i.e. includes spacing and labelling)'''

    # If there are no tasks, print a message indicating that
    if not task_list:
        print("There are no tasks assigned.")
        return
    # Display all tasks in the task_list
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned:\
   {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date:\
        {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine():
    '''Reads the task from task.txt file and prints to the console in the
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
       Allows the user to select a task by entering the corresponding number
       Allows the user to edit or mark the selected task'''

    # If the user has no tasks, print a message indicating that
    if not task_list:
        print("You have no tasks assigned.")
        return
    # Display the tasks assigned to the current user
    for i, t in enumerate(task_list, start=1):
        if t['username'] == curr_user:
            print(f"{i}. {t['title']} (Due:\
{t['due_date'].strftime(DATETIME_STRING_FORMAT)})")
    # Allow the user to go back to the main menu with '-1'
    print("-1. Go back to main menu")
    # Allows the user to select a task by entering a number
    while True:
        try:
            task_choice = int(input("Enter your choice: "))
            if task_choice == -1:
                return
            elif 1 <= task_choice <= len(task_list):
                selected_task = task_list[task_choice - 1]
                if selected_task['username'] != curr_user:
                    print("You can only view your own tasks.")
                    continue
                disp_str = f"Task: \t\t {selected_task['title']}\n"
                disp_str += f"Assigned to: \t {selected_task['username']}\n"
                disp_str += (
                    f"Date Assigned: \t "
                    f"{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                )
                disp_str += (
                    f"Due Date: \t "
                    f"{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                )
                disp_str += (
                    f"Completed: "
                    f"\t {'Yes' if selected_task['completed'] else 'No'}\n"
                )
                disp_str += f"Task Description:\
                      \n {selected_task['description']}\n"
                print(disp_str)
                # Asks if the user wants to mark or edit the task
                # If the task is already completed, inform the user
                # and allow them to choose a different task
                if selected_task['completed']:
                    print("This task is already completed.\n"
                          "-1 to go back to main menu.\n"
                          "Or select a different task.")
                    continue
                # If the task is not completed, ask the user if they want
                # to mark it as complete, edit it, or go back to the main menu
                mark_or_edit = input(
                    "Do you want to mark this task or edit it?"
                    " (mark/edit)\n"
                    "Or '-1' to go back to main menu: "
                ).strip().lower()
                if mark_or_edit == '-1':
                    return
                # If the user enters an invalid choice
                # prompt them to try again
                if mark_or_edit not in ['mark', 'edit']:
                    print(
                        "Invalid choice."
                        " Please re-enter the task you want: "
                    )
                    continue
                # If the user chooses to mark or edit the task
                # Allow them to edit the assigned user and due date
                if mark_or_edit == 'edit':
                    edit_choice = input(
                        "Assign new user (Or enter to keep current): "
                    )
                    if edit_choice == '-1':
                        return
                    if edit_choice:
                        # Check if the new user exists
                        # in the username_password dictionary
                        if edit_choice not in username_password.keys():
                            print(
                                "User does not exist.\
 Please enter a valid username"
                            )
                            return
                        selected_task['username'] = edit_choice
                        # Update the task's username
                        # and inform the user
                        print(f"Task assigned to {edit_choice}.")
                    # Allow the user to edit the due date
                    due_date_choice = input(
                        "Enter new due date (YYYY-MM-DD)\
 (Or enter to keep current): ")
                    if due_date_choice:
                        # Check if the new due date is valid
                        # If not, inform the user and keep the current due date
                        try:
                            new_due_date = datetime.strptime(
                                due_date_choice, DATETIME_STRING_FORMAT)
                            selected_task['due_date'] = new_due_date
                            # Update the task's due date
                            # and inform the user
                            print(
                                f"Due date updated to "
                                f"{new_due_date.strftime(DATETIME_STRING_FORMAT)}."
                            )
                        except ValueError:
                            # If the date format is incorrect
                            # inform the user and keep the current due date
                            print(
                                "Invalid date format."
                                " Keeping current due date."
                                )
                # If the user chooses to mark the task
                # Ask if they want to mark it as complete or uncomplete
                edit_choice = input(
                    "Do you want to mark this task as complete? (yes/no):"
                    ).strip().lower()
                # If the user enters 'yes', mark the task as complete
                if edit_choice == 'yes':
                    selected_task['completed'] = True
                    print("Task marked as complete.")
                if edit_choice not in ['yes', 'no']:
                    # If the user enters an invalid choice
                    # inform them and return to the main menu
                    print("Invalid choice. Please start over.")
                    return
                # If the user enters 'no', mark the task as not complete
                elif edit_choice == 'no':
                    selected_task['completed'] = False
                    print("Task marked as not complete.")
                return
            # If the user enters an invalid choice
            # inform them and prompt them to try again
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def generate_report():
    '''Generate a report of all tasks and users and save it to a file
       task_overview.txt and user_overview.txt'''
    num_tasks = len(task_list)
    with open("task_overview.txt", "w") as task_file:
        print("")
        disp_str = f"Total tasks: \t\t\t\t{num_tasks}\n"
        # The total number of completed tasks
        completed_tasks = sum(1 for task in task_list if task['completed'])
        disp_str += f"Total completed tasks: \t\t\t{completed_tasks}\n"
        # The total number of incomplete tasks
        incomplete_tasks = num_tasks - completed_tasks
        disp_str += f"Total incomplete tasks: \t\t{incomplete_tasks}\n"
        # The total number of tasks that haven't been completed
        # by their due date
        overdue_tasks = sum(
            1 for task in task_list if not task[
                'completed'] and task['due_date'] < datetime.now())
        disp_str += f"Total overdue tasks: \t\t\t{overdue_tasks}\n"
        # The percentage of tasks that are incomplete
        if num_tasks > 0:
            incomplete_percentage = (incomplete_tasks / num_tasks) * 100
        else:
            incomplete_percentage = 0
        disp_str += f"Percentage of incomplete tasks:\
         {incomplete_percentage:.2f}%\n"
        # The percentage of tasks that are overdue
        if num_tasks > 0:
            overdue_percentage = (overdue_tasks / num_tasks) * 100
        else:
            overdue_percentage = 0
        disp_str += f"Percentage of overdue tasks:\
            {overdue_percentage:.2f}%\n"
        task_file.write(disp_str + "\n")
        print(disp_str)
    num_users = len(username_password.keys())
    with open("user_overview.txt", "w") as user_file:
        disp_str = f"Total users: \t\t{num_users}\n"
        # The total number of tasks that have been generated
        disp_str += f"Total tasks: \t\t{num_tasks}\n"
        user_file.write(disp_str + "\n")
        print(disp_str)
        # For each user, write their username
        # And the number of tasks assigned to them
        for user in username_password.keys():
            user_tasks = [t for t in task_list if t['username'] == user]
            num_user_tasks = len(user_tasks)
            disp_str = f"{user}: {num_user_tasks} tasks\n"
            # The percentage of tasks assigned to this user
            if num_tasks > 0:
                user_task_percentage = (num_user_tasks / num_tasks) * 100
            else:
                user_task_percentage = 0
            disp_str += (
                f"Percentage tasks assigned"
                f" to {user}: \t{user_task_percentage:.2f}%\n"
            )
            # The percentage of tasks assigned to this user that are completed
            completed_user_tasks = sum(1 for t in user_tasks if t['completed'])
            if num_user_tasks > 0:
                user_completed_percentage = (
                    completed_user_tasks / num_user_tasks) * 100
            else:
                user_completed_percentage = 0
            disp_str += (
                f"Percentage tasks completed by"
                f" {user}: \t{user_completed_percentage:.2f}%\n"
            )
            # The percetage of tasks that user must still complete
            incomplete_user_tasks = num_user_tasks - completed_user_tasks
            if num_user_tasks > 0:
                user_incomplete_percentage = (
                    incomplete_user_tasks / num_user_tasks) * 100
            else:
                user_incomplete_percentage = 0
            disp_str += (
                f"Percentage tasks incomplete by"
                f" {user}: \t{user_incomplete_percentage:.2f}%\n"
            )
            # The percentage of tasks that are overdue for this user
            overdue_user_tasks = sum(
                1 for t in user_tasks
                if not t['completed']
                and t['due_date'] < datetime.now()
            )
            if num_user_tasks > 0:
                user_overdue_percentage = (
                    overdue_user_tasks / num_user_tasks) * 100
            else:
                user_overdue_percentage = 0
            disp_str += (
                f"Percentage tasks overdue for"
                f" {user}: \t{user_overdue_percentage:.2f}%\n"
            )
            user_file.write(disp_str)
            print(disp_str)


# ====Reading tasks from file====


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # If the user is an admin, they can register a new user.
    if menu == 'r' and curr_user == 'admin':
        '''If the user is an admin they can register a new user.'''
        reg_user()
        continue
    # If the user is not an admin, they cannot register a new user.
    elif menu == 'r' and curr_user != 'admin':
        print("You do not have permission to register a new user.")
        continue

    elif menu == 'a':
        '''Allow a user to add new task to the task.txt file'''
        add_task()
        continue

    elif menu == 'va' and curr_user == 'admin':
        '''If the user is an admin they can view all tasks.
        if the user is not an admin, they can only view their own tasks.'''
        view_all()
        continue

    elif menu == 'va' and curr_user != 'admin':
        '''If the user is not an admin, they can only view their own tasks.
           Display the tasks assigned to the current user.'''
        if not any(t['username'] == curr_user for t in task_list):
            print("You have no tasks assigned.")
            continue
        print("You can only view your tasks:")
        view_mine()
        continue

    elif menu == 'vm':
        '''gives the user the option to view their own tasks.'''
        print("Your tasks:")
        view_mine()
        continue

    elif menu == 'gr':
        '''Generate a report of all tasks and users and save it to a file
           task_overview.txt and user_overview.txt'''
        generate_report()
        print("Reports generated successfully.")
        continue

    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics
           about number of users and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")
        continue
    # If the user chooses to exit, the program will terminate.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # If the user makes a wrong choice, prompt them to try again.
    else:
        print("You have made a wrong choice, Please Try again")
        continue
