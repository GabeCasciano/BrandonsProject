class Person:
    def __init__(self, name: str = None,  age: int = 0):
        self.name = name
        self.age = age
        self.is_here = False

    def check_in(self):
        if not self.is_here:
            self.is_here = True

    def check_out(self):
        if self.is_here:
            self.is_here = False

    def change_name(self, name: str):
        self.name = name

    def change_age(self, age: int):
        self.age = age

    def __eq__(self, other):
        if other.name == self.name and other.age == self.age:
            return True
        return False
