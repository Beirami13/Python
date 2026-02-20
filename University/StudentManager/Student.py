import User
class Student(User):

    student = []
    stuCount = 0

    def __init__(self, name, family, id, password):
        super().__init__(name, family, id, password)
        Student.stuCount += 1
        self.grades = []
        self.absences = 0
        self.confirmed_grades = []


