"""
Program: Student.py
Author: Tony Ehlert
Last date modified: 3/31/2023

The purpose of this program is define and create a Student class being derived from a Person class
and its method along with student objects
The input is required data needed to create and test objects create from the Student class
The output is print statements of each variable that come from the display() method contained in the Student class
"""
import datetime

from Topic1.Person import Person


class Student(Person):
    """Student class using base class Person"""

    def __init__(self, student_id, lname, fname, major="Computer Science", gpa=0.0, addy='', ):
        super().__init__(lname, fname, addy)
        self._major = major
        self._gpa = gpa
        self._student_id = student_id

    def change_major(self, value):
        self._major = value

    def update_gpa(self, value):
        self._gpa = value

    def display(self):
        '''
        This method returns a formatted string containing the employee object first_name, last_name,
        address (if present), major, gpa, and student id

        :return: Formatted string containing student object information
        '''
        if (self._address == ''):
            return str(
                self._last_name + ", " + self._first_name + ":(" + str(
                    self._student_id) + ") " + self._major + " gpa: " + str(self._gpa))
        else:
            return str(
                self._last_name + ", " + self._first_name + ":(" + str(
                    self._student_id) + ") " + self._major + " gpa: " + str(
                    self._gpa) + "address: " + self._address.display())

    def __str__(self):
        return ("Student ID: " + str(
            self._student_id) + ", Last Name: " + self._last_name + ", First Name: " + self._first_name + ", Major: " + self._major + ", GPA: " + str(
            self._gpa))

    def __repr__(self):
        return ("Student(" + str(
            self._student_id) + ", \'" + self._last_name + "\', \'" + self._first_name + "\', \'" + self._major + "\', " + str(
            self._gpa) + ")")


if __name__ == "__main__":
    # Driver
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    #print(my_student)
    #print(my_student.__repr__())
    del my_student
