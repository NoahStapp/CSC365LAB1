import pandas as pd


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
    print(students)


if __name__ == "__main__":
    main()
