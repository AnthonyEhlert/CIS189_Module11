"""
Program: Manager.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is to define a Manager class with private variables and overrides the derived
classes' display method, __str__, and __repr__ methods.  It also contains a give_raise method

The input is the required data needed to create and test objects create from the Manager class
The output is print statements of each variable that come from the display() method contained in the Manager
class
"""
import datetime

from Topic5.Employee import Employee
from Topic5.Person import Person


class Manager(Employee, Person):
    '''Manager class derived from Employee and Person classes'''

    def __init__(self, lname, fname, address, phone_num, start_date, slry, department, direct_reports=[]):
        Employee.__init__(self, start_date=start_date, slry=slry)
        Person.__init__(self, lname=lname, fname=fname, address=address, phone_num=phone_num)
        self._department = department
        self._direct_reports = direct_reports

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    @property
    def direct_reports(self):
        return self._direct_reports

    def add_direct_reports(self, direct_reports_list):
        """
        This method adds a list of employees to the Manager objects current direct_reports list
        :param direct_reports_list: list of Employee objects to add
        :return: N/A
        """
        self._direct_reports.append(direct_reports_list)

    def give_raise(self, value):
        """
        This method updates the salary of the Manager object
        :param value: new salary value
        :return: N/A
        """
        super().give_raise(value)

    def display(self):
        """
        This method returns a string contain information about the object

        :return:formatted string containing various variables from the object
        """
        display_string = Person.display(self) + "\n"
        display_string += Employee.display(self) + "\n"
        display_string += "Department: " + self._department + "\n"
        display_string += "Direct Reports: "
        for employees in self._direct_reports:
            display_string += (f"\n{employees})")
            # f", Start Date: {employee._start_date}, Salary: {employee._salary}")
        return display_string

    def __str__(self):
        str_string = Person.get_last_name(self) + ", "
        str_string += Person.get_first_name(self) + ", "
        str_string += Person.get_address(self).replace('\n', ' ') + ", "
        str_string += Person.get_phone_number(self) + ", "
        str_string += str(Employee.get_salary(self)) + ", "
        str_string += str(Employee.get_start_date(self)) + ", "
        str_string += self._department + ", "
        str_string += str(self._direct_reports)
        return str_string

    def __repr__(self):
        repr_string = "Manager(\""
        repr_string += Person.get_last_name(self) + "\", \""
        repr_string += Person.get_first_name(self) + "\", \""
        repr_string += Person.get_address(self).replace('\n', '\\' + 'n') + "\", \""
        repr_string += Person.get_phone_number(self) + "\", "
        repr_string += str(Employee.get_salary(self)) + ", "
        repr_string += str(Employee.get_start_date(self)) + ", \""
        repr_string += self._department + "\", "
        repr_string += str(self._direct_reports)
        return repr_string


# driver
if __name__ == "__main__":
    # create a Manager object
    service_manager = Manager("Ehlert", "Tony", "456 Sesame Street\nAnkeny, Iowa", "515-555-7777",
                              datetime.date.today(), 40000, "Service")

    # display Manager object
    print(service_manager.display())

    # create at least three direct_reports that report to Manager
    emp1 = Employee(datetime.date.today(), 25000)
    emp2 = Employee(datetime.date.today(), 27500)
    emp3 = Employee(datetime.date.today(), 30000)

    emp_list = [emp1, emp2, emp3]

    service_manager.add_direct_reports(emp_list)

    # display Manager object's direct_reports including Employee object name, start_date, salary
    print("\n")
    print(service_manager.display())

    # change salary to $42,000
    service_manager.give_raise(42000)

    # display manager object
    print("\n")
    print(service_manager.display())

    # test of __str__ and __repr__ methods
    print("\n TEST OF __str__ & __repr__ METHODS: ")
    print(service_manager)
    print(service_manager.__repr__())

    # garbage collection
    del (emp_list)
    del (emp1, emp2, emp3)
    del (service_manager)
