from .Person import Person

class Coach(Person):
    
    def __init__(self, name: str = None, age: int = 0, education: int = 0):
        super(Coach, self).__init__(name, age)
