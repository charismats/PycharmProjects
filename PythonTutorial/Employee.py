from __future__ import print_function

from Person import Person


class Employee(Person):

    def __init__(self):
        super(Employee, self).__init__()
        self.salary = 100