from Student import Student
from Subject import Subject
import logging
import json


class SchoolRegister():

    def __init__(self):
        self.studentRegister = {}

    def add_student(self, student: Student):
        self.studentRegister[student] = {}
        return self

    def get_student(self, student: Student):
        self.studentRegister[student] = {}
        return self

    def add_grade_for_subject(self, student: Student, subject: Subject, grade: int):
        if student in self.studentRegister and subject in self.studentRegister[student]:
            self.studentRegister[student][subject] += (grade,)
        elif student in self.studentRegister and subject not in self.studentRegister[student]:
            self.studentRegister[student][subject] = (grade,)
        else:
            self.studentRegister[student] = {}
            self.studentRegister[student][subject] = (grade,)
        return self

    def add_subject(self, student, subject):
        self.studentRegister[student][subject] = None

    # @staticmethod
    # def add_grade_for_student(studentDict):
    #     print(studentDict)

    # def for_student(self, student: Student):
    #     if student in self.studentRegister:
    #         return self.studentRegister
    #     else:
    #         logging.error("such student does not exist in the register!")

    def display_school_register(self):
        print(self.studentRegister)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def export_register_to_JSON(self, filePath):
        # dictToSave = stringify_keys(self.studentRegister)
        with open(filePath, 'w') as fp:
            json.dump(dictToSave, fp)
            # fp.write(json.dumps(list(self.studentRegister.items())))



def stringify_keys(d):
    """Convert a dict's keys to strings if they are not."""
    for key in d.keys():

        # check inner dict
        if isinstance(d[key], dict):
            value = stringify_keys(d[key])
        else:
            value = d[key]

        # convert nonstring to string if needed
        if not isinstance(key, str):
            try:
                d[str(key)] = value
            except Exception:
                try:
                    d[repr(key)] = value
                except Exception:
                    raise

            # delete old key
            del d[key]
    return d


if __name__ == '__main__':
    logging.info("this file is not meant to be run directly")
