from Student import Student
import logging


class Diary():

    def __init__(self):
        self.studentList = [] 
        
    def add_student(self, student):
        self.studentList.append(student)

    def add_grade_for_student(self, grade, student):
        next(x for x in self.studentList if x student)


if __name__ == '__main__':
    logging.info("this file is not meant to be run directly")