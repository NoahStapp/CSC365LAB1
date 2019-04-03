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
    #studentInfo(students, "COMO")
    #studentBusRoute(students, "COMO")
    #teacherStudents(students, "HANTZ", "JED")
    #busRoute(students, 52)
    #gradeLevel(students, 3)
    maxGradeLevel(students, 3)
    #print(students)

def studentInfo(students, name):
    print(students.loc[students['lastName'] == name][['grade', 'classroom', 'teacherLastName', 'teacherFirstName']])

def studentBusRoute(students, name):
    print(students.loc[students['lastName'] == name]['bus'])

def teacherStudents(students, lastName, firstName):
    print(students.loc[(students['teacherFirstName'] == firstName) & (students['teacherLastName'] == lastName)][['lastName', 'firstName']])

def busRoute(students, busRoute):
    print(students.loc[students['bus'] == busRoute][['lastName', 'firstName']])

def gradeLevel(students, grade):
    print(students.loc[students['grade'] == grade][['lastName', 'firstName']])

def avgGradeLevel(students, grade):
    print(students.loc[students['grade'] == grade]['GPA'].mean())

def maxGradeLevel(students, grade):
    print(students.loc[students['grade'] == grade]['GPA'].max())




if __name__ == "__main__":
    main()
