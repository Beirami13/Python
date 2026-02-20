import Student

class StudentHandler:
    students = []

    @classmethod
    def addStudent(cls, name, family, password):
        student_id = len(cls.students) + 1
        student = Student.Student(name, family, id, password)
        cls.students.append(student)
        print(f"successfully signed up yor ID is: {student_id}")
        return student

    @classmethod
    def login(cls, name, password):
        for student in cls.students:
            if student.name == name and student.password == password:
                return student
        return None

    @classmethod
    def findStudent(cls, name, password):
        for student in cls.students:
            if student.name == name and student.password == password:
                return student

