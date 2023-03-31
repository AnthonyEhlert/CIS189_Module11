"""
Program: HourlyEmployee.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is to define a HourlyEmployee class with private variables and overrides the derived
class' display method, __str__, and __repr__ methods.  It also contains a give_raise method

The input is the required data needed to create and test objects create from the HourlyEmployee class
The output is print statements of each variable that come from the display() method contained in the HourlyEmployee
class
"""
import datetime

from Topic4.Employee import Employee


class HourlyEmployee(Employee):
    '''HourlyEmployee Class derived from Employee class'''

    def __init__(self, lname, fname, address, phone_num, start_date, slry):
        super().__init__(lname, fname, address, phone_num)
        self._start_date = start_date
        self._hourly_pay = slry

    # getters and setter

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_start_date(self):
        return self._start_date

    def set_hourly_pay(self, salary):
        self._hourly_pay = salary

    def get_hourly_pay(self):
        return self._hourly_pay

    # give_raise method
    def give_raise(self, value):
        """
        This method updates the hourly_pay for the object

        :param value: new hourly_pay
        :return: N/A
        """
        self._hourly_pay = value

    def display(self):
        """
        This method returns a string value with the values of the object's variables (excluding phone_number)

        :return: Formatted string of values of object's variables
        """
        display_string = super().display()
        display_string = display_string + "\nHourly employee: $" + str(f"{self._hourly_pay:.2f}/hour")
        display_string = display_string + "\nStart Date: " + str(f"{self._start_date:%m-%e-%Y}".lstrip('0'))
        return display_string

    def __str__(self):
        str_string = "Last Name: " + self._last_name
        str_string = str_string + (", First Name: " + self._first_name)
        str_string = str_string + (", Address: " + str(self._address).replace('\n', ' '))
        str_string = str_string + (", Phone #: " + self._phone_number)
        str_string = str_string + (", Start Date: " + str(self._start_date))
        str_string = str_string + (", Hourly Pay: " + str(self._hourly_pay))
        return str_string

    def __repr__(self):
        repr_string = "HourlyEmployee(\"" + self._last_name
        repr_string = repr_string + ("\", \"" + self._first_name)
        repr_string = repr_string + ("\", \"" + str(self._address).replace('\n', '\\' + 'n'))
        repr_string = repr_string + ("\", \"" + self._phone_number)
        repr_string = repr_string + ("\", " + str(self._start_date))
        repr_string = repr_string + (", " + str(self._hourly_pay) + ")")
        return repr_string


# Driver
if __name__ == "__main__":
    # create and HourlyEmployee object
    first_shift_emp1 = HourlyEmployee("Ehlert", "Tony", "456 Sesame Street\nAnkeny, Iowa", "515-555-7777",
                                      datetime.date.today(), 10.00)

    # display the Employee object
    print(first_shift_emp1.display())

    # change hourly_pay to $12.00
    first_shift_emp1.give_raise(12.00)

    # display the Employee object
    print("\n")
    print(first_shift_emp1.display())

    # test of __str__ and __repr__ methods
    print("\ntest of __str__ & __repr__ strings:")
    print(first_shift_emp1)
    print(first_shift_emp1.__repr__())

    # garbage collection
    del (first_shift_emp1)
