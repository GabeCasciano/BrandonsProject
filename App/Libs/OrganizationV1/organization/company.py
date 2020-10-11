from .employee import employee
from .person import person
from .client import client
from .schedule import appointment, schedule

from datetime import datetime

class company:

    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.clients = []
        self.org_number = 1

    def add_employee(self, name: str = None, age: int = None, emp: person = None):
        if emp != None:
            for e in self.employees:
                if e.organization_number == emp.organization_number:
                    return False
            self.employees.append(emp)
        else:
            emp = employee(name, age, self.org_number)
            self.org_number += 1
            self.employees.append(emp)

    def add_customer(self, name: str = None, age: int = None, cust: person = None):
        if cust != None:
            for c in self.clients:
                if c.organization_number == cust.organization_number:
                    return False
            self.clients.append(cust)
        else:
            cust = client(name, age, self.org_number)
            self.org_number += 1
            self.employees.append(cust)

    def book_employee(self, date: datetime, employee: employee, client: client):
        for e in self.employees:
            if e.organization_number == employee.organization_number:
                e.book(date, client)
                break

    def toggle_location(self, person: person):
        for e in self.employees:
            if e.organization_number == person.organization_number:
                if e.present == False:
                    e.check_in()
                else:
                    e.check_out()
                return
        for c in self.clients:
            if c.organization_number == person.organization_number:
                if e.present == False:
                    e.check_in()
                else:
                    e.check_out()
                return

    def get_info(self):
        emp = []
        cust = []
        for e in self.employees:
            emp.append(e.format_csv())
        for c in self.clients:
            cust.append(c.format_csv())

        return emp, cust

    def get_person_info(self, name: str = None, number: int = None):
        if number != None:
            for e in self.employees:
                if e.organization_number == number:
                    return e
            for c in self.clients:
                if c.organization_number == number:
                    return c
        if name != None:
            for e in self.employees:
                if e.name == name:
                    return e
            for c in self.clients:
                if c.name == name:
                    return c
        return None

