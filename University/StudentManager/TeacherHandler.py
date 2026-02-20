import StudentHandler
import Teacher

class TeacherHandler:

    @staticmethod
    def SetGrade(student_name, grade):
        students = StudentHandler.StudentHandler.students
        for student in students:
            if student.name == student_name:
                if not hasattr(student, 'grades'):
                    student.grades = []
                student.grades.append(grade)
                print(f"Grade {grade} set for {student_name}")
                return True
        print(f"Student {student_name} not found")
        return False

    @staticmethod
    def SetAbsence(student_name):
        students = StudentHandler.StudentHandler.students
        for student in students:
            if student.name == student_name:
                if not hasattr(student, 'absences'):
                    student.absences = []
                student.absences+=1
                print(f"Absence set for {student_name}")
                return True
        print(f"Student {student_name} not found")
        return False

    @classmethod
    def editInfo(cls, info):
        match info:
            case "name":
                Teacher.Teacher.name = input("Enter your name: ")
            case "family":
                Teacher.Teacher.family = input("Enter your family: ")
            case "password":
                Teacher.Teacher.password = input("Enter your password: ")
            case _:
                print("Invalid info")
