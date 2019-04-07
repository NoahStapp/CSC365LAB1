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

    while 1:
        user_input = input("").split(" ")

        if user_input[0] == "Q" or user_input[0] == "Quit":
            break
        elif (user_input[0] == "S:" or user_input[0] == "Student:") and user_input[1].isalpha():
            if len(user_input) == 2:
                studentInfo(students, user_input[1].upper())
            else:
                studentInfoBusRoute(students, user_input[1].upper())
        elif (user_input[0] == "T:" or user_input[0] == "Teacher:") and user_input[1].isalpha():
            teacherStudents(students, user_input[1].upper())
        elif (user_input[0] == "B:" or user_input[0] == "Bus:") and user_input[1].isnumeric():
            busRoute(students, int(user_input[1]))
        elif user_input[0] == "A:" or user_input[0] == "Average:" and user_input[1].isnumeric():
            avgGradeLevel(students, int(user_input[1]))
        elif user_input[0] == "I" or user_input[0] == "Info":
            for i in range(0, 7):
                studentsPerGrade(students, i)
        elif (user_input[0] == "G:" or user_input[0] == "Grade:") and user_input[1].isnumeric():
            if len(user_input) == 3:
                if user_input[2] == "H" or user_input[2] == "High":
                    minMaxGradeLevel(students, int(user_input[1]), "max")
                elif user_input[2] == "L" or user_input[2] == "Low":
                    minMaxGradeLevel(students, int(user_input[1]), "min")
            else:
                gradeLevel(students, int(user_input[1]))


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
        ].values
    )


def studentInfoBusRoute(students, name):
    print(students.loc[students["lastName"] == name][["lastName", "firstName", "bus"]].values)


def teacherStudents(students, lastName):
    print(
        students.loc[(students["teacherLastName"] == lastName)][
            ["lastName", "firstName"]
        ].values
    )


def busRoute(students, busRoute):
    print(students.loc[students["bus"] == busRoute][["lastName", "firstName"]].values)


def gradeLevel(students, grade):
    print(students.loc[students["grade"] == grade][["lastName", "firstName"]].values)


def avgGradeLevel(students, grade):
    print(students.loc[students["grade"] == grade]["GPA"].mean())


def minMaxGradeLevel(students, grade, flag):

    if(students[students["grade"] == grade].size):
        if flag == "max":
            print(
                students.loc[students.loc[students["grade"] == grade]["GPA"].idxmax()][
                    [
                        "lastName",
                        "firstName",
                        "GPA",
                        "teacherLastName",
                        "teacherFirstName",
                        "bus",
                    ]
                ].values
            )
        else:
            print(
                students.loc[students.loc[students["grade"] == grade]["GPA"].idxmin()][
                    [
                        "lastName",
                        "firstName",
                        "GPA",
                        "teacherLastName",
                        "teacherFirstName",
                        "bus",
                    ]
                ].values
            )


def studentsPerGrade(students, grade):
    print(grade, ": ", len(students.loc[students["grade"] == grade].values))


if __name__ == "__main__":
    main()
