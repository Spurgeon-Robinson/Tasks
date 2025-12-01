# Take user inputs for name, age, hair color, and eye color
def get_user_inputs():
    user_inputs = {}
    prompts = {
        "name": "Please enter your name: ",
        "age": "Please enter your age (must be 0 or greater): ",
        "hair_color": "Please enter your hair color: ",
        "eye_color": "Please enter your eye color: ",
    }
    # Validate inputs and reprompt if invalid
    # Name, hair color, and eye color should contain only letters
    # Age should be a number 0 or greater
    for key, prompt in prompts.items():
        while True:
            user_input = input(prompt)
            if key == "name":
                if user_input.isalpha():
                    user_inputs[key] = user_input
                    break
                else:
                    print("Invalid input. Name must contain only letters.")
            elif key == "age":
                if user_input.isdigit() and int(user_input) >= 0:
                    user_inputs[key] = int(user_input)
                    break
                else:
                    print("Invalid input. Age must be a number 0 or greater.")
            else:
                if user_input.isalpha():
                    user_inputs[key] = user_input
                    break
                else:
                    print(
                        f"Invalid input. {key.replace('_', ' ').capitalize()}"
                        " must contain only letters"
                    )

    # Determine if user is an adult or child and create appropriate object
    if user_inputs["age"] > 124:
        person = Lier(
            user_inputs["name"],
            user_inputs["age"],
            user_inputs["hair_color"],
            user_inputs["eye_color"],
        )
        person.can_lie()
    elif user_inputs["age"] < 123 and user_inputs["age"] >= 18:
        person = Adult(
            user_inputs["name"],
            user_inputs["age"],
            user_inputs["hair_color"],
            user_inputs["eye_color"],
        )
        person.can_drive()
    elif user_inputs["age"] < 18:
        person = Child(
            user_inputs["name"],
            user_inputs["age"],
            user_inputs["hair_color"],
            user_inputs["eye_color"],
        )
        person.can_drive()


# Create class Adult
class Adult:
    # Initialize the class with name, age, hair color, and eye color
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def can_drive(self):
        print(f"{self.name} is an adult and can drive.")


# Create subclass Child
class Child(Adult):
    # Initialize the class with name, age, hair color, and eye color
    def __init__(self, name, age, hair_color, eye_color):
        super().__init__(name, age, hair_color, eye_color)

    def can_drive(self):
        print(f"{self.name} is a child and cannot drive.")


# Create Lier subclass
class Lier(Adult):
    # Initialize the class with name, age, hair color, and eye color
    def __init__(self, name, age, hair_color, eye_color):
        super().__init__(name, age, hair_color, eye_color)

    def can_lie(self):
        print(f"{self.name} is a liar.")


get_user_inputs()
