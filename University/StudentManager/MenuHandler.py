import StudentHandler
import TeacherHandler

def mainMenu():
    while True:
        print("\n=== University Library Management System ===")
        print("0.Exit")
        print("1.Student")
        print("2.Teacher")
        print("3.Manager")

        choice = input("Enter your choice: ")
        match choice:
            case "0":
                print("Exiting the system")
                break
            case "1":
                StudentMenu()
            case "2":
                TeacherMenu()
            case "3":
                ManagerMenu()
            case _:
                print("Invalid option! Please try again.")
        print("----------------------------------------------")


def StudentMenu():
    while True:
        print("\nDo you have account?")
        choice = input("Enter your choice: ")
        choice = choice.lower()
        if choice == "yes":
            name = input("Please enter your name: ")
            password = input("Please enter your password: ")
            student = StudentHandler.StudentHandler.findStudent(name, password)
            if student:
                print("You logged in")
                ActiveStudentMenu(student)
            else:
                print("You entered wrong password")
        elif choice == "no":
            SignUpStudentMenu()
            break
        else:
            print("Invalid option! Please try again.")


def ActiveStudentMenu(student):
    while True:
        print("\n=== Student Management System ===")
        print("0.Exit")
        print("1.Grades")
        print("2.Confirmed grades")
        print("3.Absences")

        choice = input("Enter your choice: ")
        match choice:
            case "0":
                print("Exiting the system")
                break
            case "1":
                print(student.grades)
            case "2":
                print(student.confirmed_grades)
            case "3":
                print(student.absences)
            case _:
                print("Invalid option! Please try again.")
        print("----------------------------------------------")


def SignUpStudentMenu():
    name = input("Please enter your name: ")
    family = input("Please enter your family: ")
    password = input("Please enter your password: ")
    student=StudentHandler.StudentHandler.addStudent(name, family, password)
    print("Student registered successfully!")
    choice = input("Do you want to continue?")
    choice = choice.lower()
    if choice == "yes":
        ActiveStudentMenu(student)
    elif choice == "no":
        print("Exiting the system")
    else:
        print("Invalid option! Please try again.")


def TeacherMenu():
    while True:
        password = input("Please enter your password: ")
        if password == "1234":
            print("You logged in")

            print("\n=== Teacher Management System ===")
            print("0.Exit")
            print("1.set grades")
            print("2.set absences")
            print("3.edit information")
            choice = input("Enter your choice: ")
            match choice:
                case "0":
                    print("Exiting the system")
                    break
                case "1":
                    print("seting grades")
                    name = input("Enter students name: ")
                    grade = input("Enter your grades: ")
                    TeacherHandler.TeacherHandler.SetGrade(name, grade)
                case "2":
                    print("set absences")
                    name = input("Enter students name: ")
                    TeacherHandler.TeacherHandler.SetAbsence(name)
                case "3":
                    print("edit information")
                    info = input("What do you want to edit?: ")
                    TeacherHandler.TeacherHandler.editInfo(info)
                case _:
                    print("Invalid option! Please try again.")
        else:
            print("You entered wrong password")
            break


def ManagerMenu():
    while True:
        password = input("Please enter your password: ")
        if password == "1234":
            print("You logged in")

            print("\n=== Manager Management System ===")
            print("0.Exit")
            print("1.Students information")
            print("2.Teachers information")
            print("3.Confirming grades")
            choice = input("Enter your choice: ")
            match choice:
                case "0":
                    print("Exiting the system")
                    break
                case "1":
                    print(StudentHandler.StudentHandler.students)
                case "2":
                    print("Teachers information")
                case "3":
                    print("Confirming grades")
                case _:
                    print("Invalid option! Please try again.")
        else:
            print("You entered wrong password")
            break