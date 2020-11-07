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
from statistics import mean
import math
from random import randrange


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
        schoolToReturn = {}
        schoolToReturn["schoolName"] = _school
        schoolToReturn["className"] = _class
        schoolToReturn["class"] = schoolDB[_school][_class]
        return schoolToReturn
    logging.error(
        "Class %s or school %s does not exist in the data structure!", _class, _school)
    quit()
    return None


def is_student_in_class(_student: str, _class):
    if _student in _class:
        logging.warning("Student %s is already in this class", _student)
        return True
    return False


def add_student_to_class(_student: str, _class):
    if not is_student_in_class(_student, _class["class"]):
        _class["class"][0][_student] = {}


def does_subject_exist_for_student_in_class(_subject: str, _student: str, _class):
    if _subject in _class[0][_student]:
        logging.warning(
            "Subject %s already exists for Student %s", _subject, _student)
        return True
    return False


def add_subject_for_student_in_class(_subject: str, _student: str, _class):
    if not does_subject_exist_for_student_in_class(_subject, _student, _class["class"]):
        _class["class"][0][_student][_subject] = []


def add_subject_for_all_students_in_class(_subject: str, _class):
    for student in _class["class"][0]:
        if not does_subject_exist_for_student_in_class(_subject, student, _class["class"]):
            _class["class"][0][student][_subject] = []


def get_subject_for_student_in_class(_subject: str, _student: str, _class):
    if does_subject_exist_for_student_in_class(_subject, _student, _class["class"]):
        subjectToReturn = {}
        subjectToReturn["studentName"] = _student
        subjectToReturn["subjectName"] = _subject
        subjectToReturn["marks"] = _class["class"][0][_student][_subject]
        return subjectToReturn


def get_all_subjects_for_student_in_class(_student: str, _class):
    subjectToReturn = {}
    subjectToReturn["studentName"] = _student
    for subject in _class["class"][0][_student]:
        subjectToReturn[subject] = _class["class"][0][_student][subject]
    return subjectToReturn


def add_marks_for_subject(_subject, _marksList):
    _subject.extend(_marksList)


def save_data_to_JSON(_filePath: str):
    with open(_filePath, 'w') as json_file:
        json.dump(schoolDB, json_file)
    logging.info("Sucesfully written data to file")


def get_data_from_JSON(_filePath: str):
    with open(_filePath) as json_file:
        return json.load(json_file)


def display_whole_class(_class: str):
    logging.info("Displaying class details:")
    print("School: {}, class: {}".format(
        _class["schoolName"], _class["className"]))
    for student in _class["class"][0]:
        print("{}: ".format(student), end='')
        for subject in _class["class"][0][student]:
            print("{}: {}, ".format(
                subject, _class["class"][0][student][subject]), end='')
        print("\n", end='')
    print("\n", end='')


def display_statistics_for_class(_class: str):
    logging.info("Displaying class statistics:")
    print("School: {}, class: {}".format(
        _class["schoolName"], _class["className"]))

    avgMarksForSubject = {}
    avgMarksForClass = {}
    for student in _class["class"][0]:
        print("{}: ".format(student), end='')
        avgMarksForSubject[student] = {}
        for subject in _class["class"][0][student]:
            if subject not in avgMarksForClass:
                avgMarksForClass[subject] = []
            if (len(_class["class"][0][student][subject]) == 0):
                avgMarksForSubject[student][subject] = "No Grades"
            else:
                avgMarksForSubject[student][subject] = mean(
                    _class["class"][0][student][subject])
                avgMarksForClass[subject].append(
                    avgMarksForSubject[student][subject])
            print("{}: {}, ".format(
                subject, avgMarksForSubject[student][subject]), end='')
        print("\n", end='')

    print("\nTotal class Average:")
    for subject in avgMarksForClass:
        avgMarksForClass[subject] = round_decimals_up(
            mean(avgMarksForClass[subject]))
        print("{}: {} \n".format(subject, avgMarksForClass[subject]), end='')
    print("\n", end='')


def round_decimals_up(number: float, decimals: int = 2):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)
    factor = 10 ** decimals
    return math.ceil(number * factor) / factor


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    schoolDB = {}

    add_school("UJ")
    add_class_for_school("year_2", "UJ")

    add_school("AGH")
    add_class_for_school("year_1", "AGH")
    add_class_for_school("year_3", "AGH")

    agh_year1 = get_class_in_school("year_1", "AGH")
    add_student_to_class("Yazmin Whitaker", agh_year1)
    add_student_to_class("Tasha Hastings", agh_year1)
    add_student_to_class("Farhan Gallagher", agh_year1)
    add_student_to_class("Davina Cowan", agh_year1)
    add_student_to_class("Ruari Fleming", agh_year1)
    add_student_to_class("Jae Aguirre", agh_year1)

    agh_year3 = get_class_in_school("year_3", "AGH")
    add_student_to_class("Ewan Blackwell", agh_year3)
    add_student_to_class("Mikaela Oliver", agh_year3)
    add_student_to_class("Daniele Hardin", agh_year3)
    add_student_to_class("Kelise Johnston", agh_year3)
    add_student_to_class("Devante Whitmore", agh_year3)
    add_student_to_class("Paige Drummond", agh_year3)

    uj_year2 = get_class_in_school("year_2", "UJ")
    add_student_to_class("Umar Houston", uj_year2)
    add_student_to_class("Raul Clay", uj_year2)
    add_student_to_class("Barnaby Hensley", uj_year2)
    add_student_to_class("Maude Wilson", uj_year2)
    add_student_to_class("Theo Gale", uj_year2)
    add_student_to_class("Tomasz Thornton", uj_year2)

    add_subject_for_all_students_in_class("Physics", agh_year1)
    add_subject_for_all_students_in_class("Python", agh_year3)
    add_subject_for_all_students_in_class("Literature", uj_year2)

    add_subject_for_student_in_class(
        "Maths", "Barnaby Hensley", uj_year2)

    Umar_Houston_marks = get_all_subjects_for_student_in_class(
        "Umar Houston", uj_year2)
    Raul_Clay_marks = get_all_subjects_for_student_in_class(
        "Raul Clay", uj_year2)
    Barnaby_Hensley_marks = get_all_subjects_for_student_in_class(
        "Barnaby Hensley", uj_year2)
    Maude_Wilson_marks = get_all_subjects_for_student_in_class(
        "Maude Wilson", uj_year2)
    Theo_Gale_marks = get_all_subjects_for_student_in_class(
        "Theo Gale", uj_year2)
    Tomasz_Thornton_marks = get_all_subjects_for_student_in_class(
        "Tomasz Thornton", uj_year2)

    Yazmin_Whitaker_marks = get_all_subjects_for_student_in_class(
        "Yazmin Whitaker", agh_year1)
    Tasha_Hastings_marks = get_all_subjects_for_student_in_class(
        "Tasha Hastings", agh_year1)
    Farhan_Gallagher_marks = get_all_subjects_for_student_in_class(
        "Farhan Gallagher", agh_year1)
    Davina_Cowan_marks = get_all_subjects_for_student_in_class(
        "Davina Cowan", agh_year1)
    Ruari_Fleming_marks = get_all_subjects_for_student_in_class(
        "Ruari Fleming", agh_year1)
    Jae_Aguirre_marks = get_all_subjects_for_student_in_class(
        "Jae Aguirre", agh_year1)

    Ewan_Blackwell_marks = get_all_subjects_for_student_in_class(
        "Ewan Blackwell", agh_year3)
    Mikaela_Oliver_marks = get_all_subjects_for_student_in_class(
        "Mikaela Oliver", agh_year3)
    Daniele_Hardin_marks = get_all_subjects_for_student_in_class(
        "Daniele Hardin", agh_year3)
    Kelise_Johnston_marks = get_all_subjects_for_student_in_class(
        "Kelise Johnston", agh_year3)
    Devante_Whitmore_marks = get_all_subjects_for_student_in_class(
        "Devante Whitmore", agh_year3)
    Paige_Drummond_marks = get_all_subjects_for_student_in_class(
        "Paige Drummond", agh_year3)

    # year_2 UJ
    add_marks_for_subject(Umar_Houston_marks["Literature"], [2, 2, 1, 3])
    add_marks_for_subject(Raul_Clay_marks["Literature"], [4, 5, 3, 2, 1])
    add_marks_for_subject(Barnaby_Hensley_marks["Literature"], [4, 1, 1, 2, 3])
    add_marks_for_subject(Maude_Wilson_marks["Literature"], [1, 3, 4, 5, 2])
    add_marks_for_subject(Theo_Gale_marks["Literature"], [3, 4, 5, 2, 2])
    add_marks_for_subject(Tomasz_Thornton_marks["Literature"], [2, 5, 4, 1, 3])

    add_marks_for_subject(Barnaby_Hensley_marks["Maths"], [4, 2, 3, 1, 5])

    # year_1 AGH
    add_marks_for_subject(Yazmin_Whitaker_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Tasha_Hastings_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Farhan_Gallagher_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Davina_Cowan_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Ruari_Fleming_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Jae_Aguirre_marks["Physics"], [
                          randrange(1, 5) for i in range(0, 5)])

    # year_3 AGH
    add_marks_for_subject(Ewan_Blackwell_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Mikaela_Oliver_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Daniele_Hardin_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Kelise_Johnston_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Devante_Whitmore_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])
    add_marks_for_subject(Paige_Drummond_marks["Python"], [
                          randrange(1, 5) for i in range(0, 5)])

    display_whole_class(agh_year1)
    display_statistics_for_class(agh_year1)
    display_whole_class(agh_year3)
    display_statistics_for_class(agh_year3)
    display_whole_class(uj_year2)
    display_statistics_for_class(uj_year2)

    save_data_to_JSON('result.json')

    schoolDB_2 = get_data_from_JSON('result.json')
