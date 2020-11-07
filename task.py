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
import json
import logging

# School / Class:


def is_school_already_in_dict(_school: str):
    if _school in schoolDB:
        return True
    return False


def is_class_already_in_school(_class: str, _school: str):
    if is_school_already_in_dict(_school):
        if _class in schoolDB[_school]:
            return True
    return False


def add_school(_school: str):
    schoolDB[_school] = {}


def add_class_for_school(_class: str, _school: str):
    if not is_school_already_in_dict(_school):
        add_school(_school)
    schoolDB[_school][_class] = [{}]


def get_class_in_school(_class: str, _school: str):
    if is_class_already_in_school(_class, _school):
        return schoolDB[_school][_class]
    logging.warning(
        "Such class or school does not exist in the data structure!")
    return None

# Student / Subject


def is_student_in_class(_student: str, _class):
    if _student in _class[0]:
        logging.warning("Student %s is already in this class", _student)
        return True
    return False


def add_student_to_class(_student: str, _class):
    if not is_student_in_class(_student, _class):
        _class[0][_student] = {}


def does_subject_exist_for_student_in_class(_subject: str, _student: str, _class):
    if _subject in _class[0][_student]:
        logging.warning(
            "Subject %s already exists for Student %s", _subject, _student)
        return True
    return False


def add_subject_for_student_in_class(_subject: str, _student: str, _class):
    if not does_subject_exist_for_student_in_class(_subject, _student, _class):
        _class[0][_student][_subject] = []


def get_subject_for_student_in_class(_subject: str, _student: str, _class):
    if does_subject_exist_for_student_in_class(_subject, _student, _class):
        return [_student, _subject, _class[0][_student][_subject]]

def add_marks_for_subject(_subject, *_marksList):
    _subject.extend(_marksList)

if __name__ == '__main__':
    schoolDB = {}

    add_school("AGH")
    add_class_for_school("1year", "AGH")
    add_class_for_school("1year", "UJ")
    agh_year1 = get_class_in_school("1year", "AGH")
    add_student_to_class("Michal Loska", agh_year1)
    add_subject_for_student_in_class("Physics", "Michal Loska", agh_year1)
    add_subject_for_student_in_class("Maths", "Michal Loska", agh_year1)
    
    loska_physics = get_subject_for_student_in_class(
        "Physics", "Michal Loska", agh_year1)
    
    add_marks_for_subject(loska_physics[2], 2)
    add_marks_for_subject(loska_physics[2], 4, 5)
    # print(loska_physics)
    # schoolDB["AGH"] = {}

    # schoolDB["AGH"]["1rok"] = [{}]
    # agh_1rok = schoolDB["AGH"]["1rok"]
    # agh_1rok[0]["Loska"] = {}
    # agh_1rok[0]["Loska"]["c++"] = (2,)
    # agh_1rok[0]["Kolecki"] = {}
    # agh_1rok[0]["Kolecki"]["python"] = (3,)
    # # for_school_and_class(agh_1rok)

    # # print(agh_1rok)
    # print(agh_1rok[0])
    print(schoolDB)
    # data = None

    # with open('result.json', 'w') as fp:
    #     json.dump(schoolDB, fp)

    # with open('result.json') as json_file:
    #     data = json.load(json_file)

    # print(data)
    # agh_1rok["loska"]["fizyja"] = 2
    # schoolDB["AGH"]["1rok"] | LISTA -> | ["LOSKA"]["fizyka"] += (3,)
    # schoolDB = ["AGH", {}]
    # print(schoolDB.index(0))
    # schoolDB = {}
    # add_school("AGH")
    # displaySchoolDB()
