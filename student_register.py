# This code will allow a user to register students for an exam
number_of_students = input("How many students are taking the exam? ")
students = []
# A for loop to register each student ID
for i in range(int(number_of_students)):
    student_ID = input("Enter student ID: ")
# Writes the student IDs to a file called reg_form.txt
    with open("reg_form.txt", "a") as reg_form_file:
        reg_form_file.write(student_ID + "...\n")
    students.append(student_ID)
