"""
Program: Person.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is to define a Person class used to create person objects
The input is required data needed to create and test objects create from the Person class
The output is print statements of each variable that come from the display() method
"""
from Topic1.Address import Address


class Person():
    '''Person Class '''

    # Constructor
    def __init__(self, lname, fname, address, phone_num):
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = phone_num

    def set_last_name(self, lname):
        self._last_name = lname

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, fname):
        self._first_name = fname

    def get_first_name(self):
        return self._first_name

    def set_address(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def set_phone_number(self, phone_num):
        self._phone_number = phone_num

    def get_phone_number(self):
        return self._phone_number

    def display(self):
        '''
        This method returns a formatted string containing the Person object first_name, last_name, address

        :return: Formatted string containing Person object information
        '''
        display_string = str(self._first_name) + " " + str(self._last_name)
        display_string = display_string + "\n" + str(self._address)
        return display_string

    def __str__(self):
        str_string = "Last Name: " + self._last_name
        str_string = str_string + (", First Name: " + self._first_name)
        str_string = str_string + (", Address: " + str(self._address).replace('\n', ' '))
        str_string = str_string + (", Phone #: " + self._phone_number)
        return str_string

    def __repr__(self):
        repr_string = "Person(\"" + self._last_name
        repr_string = repr_string + ("\", \"" + self._first_name)
        repr_string = repr_string + ("\", \"" + str(self._address).replace('\n', '\\' + 'n'))
        repr_string = repr_string + ("\", \"" + self._phone_number + "\")")
        return repr_string


if __name__ == "__main__":
    # Driver
    person1 = Person('Ruiz', 'Matthew', '456 Sesame Street\nAnkeny, Iowa', '515-555-1234')
    print(person1.display())
    print(person1)
    print(person1.__repr__())

    person2 = Person('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '515-999-9876')
    print(person2.display())

    del (person1, person2)