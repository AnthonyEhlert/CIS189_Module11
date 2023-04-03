"""
Program: Employee.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is to define an Employee class with private variables and a public display() method
The input is the required data needed to create and test objects create from the Employee class
The output is print statements of each variable that come from the display() method contained in the Employee class
"""
import datetime
from datetime import date


class Employee():
    '''Employee Class'''

    def __init__(self, lname, fname, start_date, slry):
        self._last_name = lname
        self._first_name = fname
        self._start_date = start_date
        self._salary = float(slry)

    # getters and setters
    def set_last_name(self, lname):
        self._last_name = lname

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, fname):
        self._first_name = fname

    def get_first_name(self):
        return self._first_name

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_start_date(self):
        return self._start_date

    def set_salary(self, salary):
        self._salary = float(salary)

    def get_salary(self):
        return self._salary

    # give_raise method
    def give_raise(self, value):
        """
        This method updates the salary for the object

        :param value: new salary
        :return: N/A
        """
        self._salary = value

    def display(self):
        """
        This method returns a string value with the values of the object's variables (excluding phone_number)

        :return: Formatted string of values of object's variables
        """
        display_string = ("Start Date: " + str(f"{self._start_date:%m-%e-%Y}".lstrip('0')))
        display_string += "\nSalary: $" + (f"{self._salary:,.0f}")
        return display_string

    def __str__(self):
        str_string = "Last Name: " + self._last_name + ", First Name: " + self._first_name + ", Start Date: " + str(
            self._start_date)
        str_string = str_string + (", Salary: " + str(f"{self._salary:.0f}"))
        return str_string

    def __repr__(self):
        repr_string = "Employee(\"" + self._last_name + "\", \"" + self._first_name + "\", " + str(self._start_date)
        repr_string = repr_string + ", " + str(self._salary) + ")"
        return repr_string

# driver
if __name__ == "__main__":
    emp1 = Employee("Rodgers", "Steve", datetime.date.today(), 25000)
    emp2 = Employee("Stark", "Tony", datetime.date.today(), 27500)
    emp3 = Employee("Banner", "Bruce", datetime.date.today(), 30000)

    print(emp1.display())
    print(emp1)
    print(emp1.__repr__())

    print(emp2.display())
    print(emp2)
    print(emp2.__repr__())

    print(emp3.display())
    print(emp3)
    print(emp3.__repr__())