from App.Libs.SchedulerV1.calendar.people import Student
from App.Libs.SchedulerV1.calendar.people import Coach
from datetime import datetime

class Course():

    def __init__(self, name: str = None, max_capacity: int = 10, time: datetime = None, duration: int = 1, is_weekly: bool = False):
        self.name = name
        self.max_capacity = max_capacity
        self.time = time
        self.duration = duration
        self.is_weekly = is_weekly
        self.students = []
        self.coaches = []

    def add_student(self, name: str = None, age: int = 0, grade: int = 0, student: Student = None):
        size = len(self.students)
        if name is None and age == 0 and student is not None:
            for s in self.students:
                if student != s: # __eq__ has been used so that comparisons can be made
                    self.students.append(student)
        elif name is not None:
            for s in self.students:
                if s.name != name and s.age != age and s.grade != grade:
                    self.students.append(Student(name, age, grade))

        if size < len(self.students):
            return True
        return False

    def add_coach(self, name: str = None, age: int = 0, education: str = None, coach: Coach = None):
        size = len(self.coaches)
        if name is None and age == 0 and coach is not None:
            for c in self.coaches:
                if coach != c:
                    self.coaches.append(coach)
        elif name is not None:
            for c in self.coaches:
                if c.name != name and c.age != age:
                    self.coaches.append(Coach(name, age, education))
        if size < len(self.coaches):
            return True
        return False

    def remove_student(self, name: str = None, age: int = 0, student: Student = None):
        size = len(self.students)
        if name is None and age == 0 and student is not None:
            for s in self.students:
                if student == s:
                    self.students.remove(s)
        elif name is not None:
            for s in self.students:
                if name == s.name:
                    self.students.remove(s)
        if size > len(self.students):
            return True
        return False

    def remove_coach(self, name: str = None, age: int = 0, coach: Coach = None):
        size = len(self.coaches)
        if name is None and age == 0 and coach is not None:
            for s in self.coach:
                if coach == s:
                    self.coach.remove(s)
        elif name is not None:
            for s in self.coach:
                if name == s.name:
                    self.coach.remove(s)
        if size > len(self.coach):
            return True
        return False

    def change_class_size(self, size: int = 10):
        self.max_capacity = size

    def change_class_time(self, time: datetime = None, duration: int = 1):
        if time is not None:
            self.time = time

        if duration != self.duration:
            self.duration = duration



