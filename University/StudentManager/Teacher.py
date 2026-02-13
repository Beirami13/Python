import User
class Teacher(User):
    def __init__(self, name, family, id, password):
        super().__init__(name, family, id, password)
        self.courses = []

    Teachers= []

    def addCourse(self, course):
        self.courses.append(course)

    # edit information
    def edit_information(self):
        print("\n--- Edit Teacher Information ---")
        print("1. Name")
        print("2. Family")
        print("3. Password")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")
            self.name = new_name
            print("Name updated successfully!")
        elif choice == "2":
            new_family = input("Enter new family: ")
            self.family = new_family
            print("Family updated successfully!")
        elif choice == "3":
            new_password = input("Enter new password: ")
            self.password = new_password
            print("Password updated successfully!")
        else:
            print("Invalid choice!")
