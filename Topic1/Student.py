"""
Program: Student.py
Author: Tony Ehlert
Last date modified: 3/30/2023

The purpose of this program is define and create a Student class and its method along with student objects
The input is required data needed to create and test objects create from the Student class
The output is print statements of each variable that come from the display() method contained in the Student class
"""
import datetime

from Topic1.Person import Person


class Student:
    "Student class using Person, class composition"

    def __init__(self, person, major, start_date, gpa):
        self._person = person
        self._major = major
        self._start_date = start_date
        self._gpa = gpa

    def change_major(self, value):
        self._major = value

    def update_gpa(self, value):
        self._gpa = value

    def display(self):
        return str("Person: " + self._person.display() + ", Major: " + self._major + ", Start Date: " + str(
            self._start_date) + ", GPA: " + str(self._gpa))


if __name__ == "__main__":
    # create person object
    myself = Person("Ehlert", "Tony")

    # create student object
    dmacc_student = Student(myself, "Computer Science", datetime.date(2020, 9, 1), 4.0)

    # display the student
    print(dmacc_student.display())

    # change major to "Being Awesome"
    dmacc_student.change_major("Being Awesome")

    # update gpa to 3.0
    dmacc_student.update_gpa(3.0)

    # display the student after changes
    print(dmacc_student.display())

    # garbage collection
    del (myself)
    del (dmacc_student)
