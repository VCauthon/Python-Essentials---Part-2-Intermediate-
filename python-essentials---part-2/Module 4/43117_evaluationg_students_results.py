'''

    Estimated time > 30-90 minutes
    Level of difficulty > Medium

    Objectives:
        improve the student's skills in operating with files (reading)
        perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.

    Scenario:
        Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

    The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

        The file may look as follows:
            John	Smith	5
            Anna	Boleyn	4.5
            John	Smith	2
            Anna	Boleyn	11
            Andrew	Cox	1.5
            samplefile.txt

    Your task is to write a program which:
        1.asks the user for Prof. Jekyll's file name;
        2.reads the file contents and counts the sum of the received points for each student;
        3.prints a simple (but sorted) report, just like this one:
            Andrew Cox 1.5
            Anna Boleyn 15.5
            John Smith 7.0

    output

    Note: your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
    implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

    Tip: Use a dictionary to store the students' data.
'''
import os
from os import strerror, path


class StudentsDataException(Exception):
    "Class that contains students exceptions"
    def __init__(self, message="There has been an error processing the file"):
        super().__init__(message)
        self.score = None
        self.error = "Generic students data exception"

    def check_valid_data(self, values):
        # Sets the score value to return data
        self.score = None

        # Checks if there is missing data in this line
        if len(values) == 3:
            # Checks if the score is a digit
            if values[2].isdigit():
                self.score = float(j_data[2])
            # Checks if the score is a float
            else:
                try:
                    self.score = float(j_data[2])
                except Exception:
                    raise BadLine
        else:
            raise BadLine


class BadLine(StudentsDataException):
    """This class controles if there have been some data error"""
    def __init__(self, message="There has been an error reading data from student"):
        super().__init__(message)


class FileEmpty(StudentsDataException):
    """This class controles if the file is empty"""
    def __init__(self, message="The file is empty"):
        super().__init__(message)

# Dictionary with the scores by student
students_data = {}
r_jekyll_notes = None
error_checker = StudentsDataException()
line_notes = None

# Creates a stream with the Prof. Jekyll's notes
try:
    r_jekyll_notes = open(path.join(os.getcwd(), '43117_text.txt'), mode='rt')
    line_notes = r_jekyll_notes.readlines()
    r_jekyll_notes.close()

    # Checks if the file is empty
    if len(line_notes) == 0:
        raise FileEmpty

except FileEmpty as Error:
    print(Error.args)
    quit()


for line in line_notes:

    try:
        # Splits the line by whitespaces
        j_data = line.split()

        # Checks if there is missing data in this line
        error_checker.check_valid_data(j_data)

        j_data[2] = error_checker.score
        student_name = j_data[0] + " " + j_data[1]

        # Create the student to the dictionary or accumulate the score to the existing student
        if student_name not in students_data:
            students_data[student_name] = j_data[2]
        else:
            students_data[student_name] += j_data[2]

    except BadLine as Error:
        print(Error.args)
        quit()

# Accumulates all the score's by student
print(students_data)
