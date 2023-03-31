"""
Program: SalariedEmployee.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is to define a SalariedEmployee class with private variables and overrides the derived
class' display method, __str__, and __repr__ methods.  It also contains a give_raise method

The input is the required data needed to create and test objects create from the SalariedEmployee class
The output is print statements of each variable that come from the display() method contained in the SalariedEmployee
class
"""
import datetime

from Topic4.Employee import Employee


class SalariedEmployee(Employee):
    '''SalariedEmployee Class derived from Employee class'''

    def __init__(self, lname, fname, address, phone_num, start_date, slry):
        super().__init__(lname, fname, address, phone_num)
        self._start_date = start_date
        self._salary = float(slry)

    # getters and setters
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

        :param value: new yearly salary
        :return: N/A
        """
        self._salary = value

    def display(self):
        """
        This method returns a string value with the values of the object's variables (excluding phone_number)

        :return: Formatted string of values of object's variables
        """
        display_string = super().display()
        display_string = display_string + "\nSalaried employee: $" + (f"{self._salary:,.0f}/year")
        display_string = display_string + "\nStart Date: " + str(f"{self._start_date:%m-%e-%Y}".lstrip('0'))
        return display_string

    def __str__(self):
        str_string = "Last Name: " + self._last_name
        str_string = str_string + (", First Name: " + self._first_name)
        str_string = str_string + (", Address: " + str(self._address).replace('\n', ' '))
        str_string = str_string + (", Phone #: " + self._phone_number)
        str_string = str_string + (", Start Date: " + str(self._start_date))
        str_string = str_string + (", Salary: " + str(f"{self._salary:.0f}"))
        return str_string

    def __repr__(self):
        repr_string = "SalariedEmployee(\"" + self._last_name
        repr_string = repr_string + ("\", \"" + self._first_name)
        repr_string = repr_string + ("\", \"" + str(self._address).replace('\n', '\\' + 'n'))
        repr_string = repr_string + ("\", \"" + self._phone_number)
        repr_string = repr_string + ("\", " + str(self._start_date))
        repr_string = repr_string + ", " + str(self._salary) + ")"
        return repr_string


# Driver
if __name__ == "__main__":
    # create and HourlyEmployee object
    first_shift_sup = SalariedEmployee("Ehlert", "Tony", "456 Sesame Street\nAnkeny, Iowa", "515-555-7777",
                                       datetime.date.today(), 40000)

    # display the Employee object
    print(first_shift_sup.display())

    # change hourly_pay to $45,000
    first_shift_sup.give_raise(45000.00)

    # display the Employee object
    print("\n")
    print(first_shift_sup.display())

    # test of __str__ and __repr__ methods
    print("\ntest of __str__ & __repr__ strings:")
    print(first_shift_sup)
    print(first_shift_sup.__repr__())

    # garbage collection
    del (first_shift_sup)
