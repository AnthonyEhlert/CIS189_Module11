"""
Program: Address.py
Author: Tony Ehlert
Last date modified: 3/30/2023

The purpose of this program is to define an Address class and its methods
The input is required data needed to create and test objects create from the Address class
The output is none
"""


class Address:
    """Address class for US addresses"""

    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        self._street_number = st_number
        self._street_name = st_name
        self._street_type = st_type
        self._apartment_number = apt_num
        self._city = city
        self._state = state
        self._zip_code = zip

    def display(self):
        """
        This method returns a string value with the values of the object's variables

        :return: Formatted string of values of object's variables
        """
        return (self._street_number + ' ' + self._street_name + ' ' + self._street_type + ' ' + self._apartment_number
                + '\n' + self._city + ', ' + self._state + ' ' + self._zip_code)

    def __str__(self):
        return str(str(self._street_number) + ", " + self._street_name + ", " + self._street_type + ", " + str(
            self._apartment_number) + ", " + self._city + ", " + self._state + ", " + str(self._zip_code))

    def __repr__(self):
        return str("Address(" + str(
            self._street_number) + ", \'" + self._street_name + "\', \'" + self._street_type + "\', \'" + self._city + "\', \'" + self._state + "\', " + str(
            self._zip_code) + ", " + str(self._apartment_number))
