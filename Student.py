import logging


class Student():
    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName

    def __str__(self):
        return '{} {}'.format(self.firstName, self.secondName)

    def __repr__(self):
        return '{} {}'.format(self.firstName, self.secondName)

    def __hash__(self):
        return hash((self.firstName, self.secondName))

    def __eq__(self, other):
        return (self.firstName, self.secondName) == (other.firstName, other.secondName)


if __name__ == '__main__':
    logging.info("this file is not meant to be run directly")
