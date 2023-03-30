"""
Program: Person.py
Author: Tony Ehlert
Last date modified: 3/30/2023

The purpose of this program is to define a Person class used to create person objects
The input is required data needed to create and test objects create from the Person class
The output is print statements of each variable that come from the display() method
"""
from Topic1.Address import Address


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        '''
        This method returns a formatted string containing the Person object first_name, last_name,
        address (if present)

        :return: Formatted string containing Person object information
        '''
        if (self._address == ''):
            return str(self._last_name) + ", " + str(self._first_name)
        else:
            return str(self._last_name) + ", " + str(self._first_name) + '\n'+ self._address.display()

    def __str__(self):
        return ("Last Name: " + self._last_name + ", First Name: " + self._first_name + ", Address: " + self._address.display())

    def __repr__(self):
        repr_string = "Person(\"" + self._last_name + "\", \"" + self._first_name + "\", " + self._address.__repr__() + ")"
        return repr_string


if __name__ == "__main__":
    # Driver
    addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    person1 = Person('Hammer', 'Martin', addy1)
    print(person1.display())
    print(person1)
    print(person1.__repr__())

    # apartment number is at the end. Why?
    addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
    person2 = Person('Hammer', 'Martin')
    print(person2.display())

    del (addy1, addy2)
    del (person1, person2)