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
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        if (self.address == ''):
            return str(self.last_name) + ", " + str(self.first_name)
        else:
            return str(self.last_name) + ", " + str(self.first_name) + '\n'+ self.address.display()


if __name__ == "__main__":
    # Driver
    addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    person1 = Person('Hammer', 'Martin', addy1)
    print(person1.display())

    # apartemnt number is at the end. Why?
    #addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
    person2 = Person('Hammer', 'Martin')
    print(person2.display())

    del (addy1)
    del (person1, person2)