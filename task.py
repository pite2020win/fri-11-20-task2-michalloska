# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.
from Student import Student
from SchoolRegister import SchoolRegister
from Subject import Subject
import json

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

if __name__ == '__main__':
    student1 = Student("Michal", "Loska")
    student2 = Student("Andrzej", "Duda")

    schoolRegister = SchoolRegister()
    schoolRegister.add_student(student1)
    schoolRegister.add_grade_for_subject(student1, Subject.French, 5)
    schoolRegister.add_grade_for_subject(student1, Subject.French, 2)
    schoolRegister.add_grade_for_subject(student1, Subject.Literature, 2)
    schoolRegister.add_grade_for_subject(student1, Subject.Literature, 2)
    schoolRegister.add_subject(student1, Subject.Literature, 2)
    
    # schoolRegister.for_student(student1).add_grade_for_student()

    # schoolRegister.add_student(student2)
    schoolRegister.add_grade_for_subject(student2, Subject.Law, 1)
    schoolRegister.display_school_register()
    # schoolRegister.export_register_to_JSON('data.json')
    # # dumper(schoolRegister.studentRegister)
    # with open("data.json", 'w') as fp:
    #     json.dump(schoolRegister.studentRegister, fp, default=dumper, indent=2)

