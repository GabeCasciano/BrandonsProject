from .person import person
from .employee import employee
from .schedule import appointment, schedule

from datetime import datetime


class client(person):
    def __init__(self, name: str = None, age: int = None, organization_number: int = None):
        person.__init__(name, age, organization_number)

    def book(self, date: datetime, employee: employee):
        employee.book(date, self)

