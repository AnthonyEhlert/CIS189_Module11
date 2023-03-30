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
        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)

