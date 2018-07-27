from utils import *
from mock import *
import os, random




def create_pl_female_surname(first_surname: str = "", second_surname: str = ""):
    """
    Create polish female. If input is empty, you'll get random polish surname as result
    :param first_surname:
    :param second_surname:
    :return:
    """

    if first_surname == "":
        while first_surname == second_surname:
            first_surname = random.choice(pl_surnames)
            if true_or_false(false_weight=3):
                second_surname = random.choice(pl_surnames)

    def feminize(surname):
        if surname[-1:] == "i":
            surname = replace_char(surname, -1, "a")

        return surname

    is_double_surname = (not second_surname == "")

    if is_double_surname:
        return "%s-%s" % (feminize(first_surname), feminize(second_surname))
    else:
        return feminize(first_surname)


class Person():
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return "%s %s" % (self.name, self.surname)

    def __str__(self):
        return repr(self)
