class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for the head office address
    location = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)


class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print("Trainer:", self.trainer)
        print("Course Description:", self.description)

    def show_course_id(self):
        print("Course ID: #12345")

# Create an instance of the OOPCourse class


course_1 = OOPCourse()

# Call the methods to display details
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
