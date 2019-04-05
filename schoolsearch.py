import pandas as pd
import numpy as np


class Student:
    def __init__(
        self,
        lastName,
        firstName,
        grade,
        classroom,
        bus,
        GPA,
        teacherLastName,
        teacherFirstName,
    ):
        self.lastName = lastName
        self.firstName = firstName
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.GPA = GPA
        self.teacherLastName = teacherLastName
        self.teacherFirstName = teacherFirstName


def createStudents(inputFile):
    students = pd.read_csv(inputFile, header=None)
    students.columns = [
        "lastName",
        "firstName",
        "grade",
        "classroom",
        "bus",
        "GPA",
        "teacherLastName",
        "teacherFirstName",
    ]
    return students


def main():
    students = createStudents("students.txt")
    # studentInfo(students, "COMO")
    # studentBusRoute(students, "COMO")
    # teacherStudents(students, "HANTZ", "JED")
    # busRoute(students, 52)
    # gradeLevel(students, 3)
    # maxGradeLevel(students, 3)
    # print(students)

    while 1:
        user_input = input("").split(" ")

        if user_input[0] == "Q" or user_input[0] == "Quit":
            break
        elif user_input[0] == "S:" or user_input[0] == "Student:":
            if len(user_input) == 2:
                print(studentInfo(students, user_input[1].upper()))
            else:
                print(studentInfoBusRoute(students, user_input[1].upper()))
        elif user_input[0] == "T:" or user_input[0] == "Teacher:":
            teacherStudents(students, user_input[1].upper())
        elif user_input[0] == "B:" or user_input[0] == "Bus:":
            busRoute(students, int(user_input[1]))
        elif user_input[0] == "A:" or user_input[0] == "Average":
            avgGradeLevel(students, int(user_input[1]))
        elif user_input[0] == "I" or user_input[0] == "Info":
            for i in range(0, 7):
                studentsPerGrade(students, i)


        


def studentInfo(students, name):
    print(
        students.loc[students["lastName"] == name][
            [
                "lastName",
                "firstName",
                "grade",
                "classroom",
                "teacherLastName",
                "teacherFirstName",
            ]
        ]
    )


def studentInfoBusRoute(students, name):
    print(students.loc[students["lastName"] == name][["lastName", "firstName", "bus"]])


def teacherStudents(students, lastName):
    print(
        students.loc[(students["teacherLastName"] == lastName)][
            ["lastName", "firstName"]
        ]
    )


def busRoute(students, busRoute):
    print(students.loc[students["bus"] == busRoute][["lastName", "firstName"]])


def gradeLevel(students, grade):
    print(students.loc[students["grade"] == grade][["lastName", "firstName"]])


def avgGradeLevel(students, grade):
    print(students.loc[students["grade"] == grade]["GPA"].mean())


def maxGradeLevel(students, grade):
    print(students.loc[students["grade"] == grade]["GPA"].max())

def studentsPerGrade(students, grade):
    print(grade , ": " ,len(students.loc[students["grade"] == grade]))


if __name__ == "__main__":
    main()
