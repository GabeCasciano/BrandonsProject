from .Person import Person

class Student(Person):

    def __init__(self, name: str = None, age: int = 0, grade: int = 0,):
        super(Student, self).__init__(name, age)
        self.grade = grade

    def change_grade(self, grade):
        if grade > self.grade:
            self.grade = grade