from .person import person
from .schedule import appointment, schedule

from datetime import datetime


class employee(person):
    def __init__(self, name: str = None, age: int = None, organization_number: int = None):
        person.__init__(name, age, organization_number)

    def book(self, date: datetime, customer: person):
        if self.organization_number != customer.organization_number:
            apt = self.schd.book_apt(date, self.organization_number, customer.organization_number)
            customer.book_apt(apt=apt)
