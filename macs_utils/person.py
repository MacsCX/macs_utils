from macs_utils import utils as u
from macs_utils import mock
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
            first_surname = random.choice(mock.pl_surnames)
            if u.true_or_false(false_weight=3):
                second_surname = random.choice(mock.pl_surnames)

    def feminize(surname):
        if surname[-1:] == "i":
            surname = u.replace_char(surname, -1, "a")

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

    @property
    def email(self):
        return mock.email(self.name, self.surname)

    @property # same as __repr__
    def full_name(self):
        return "%s %s" % (self.name, self.surname)

    @classmethod
    # TODO test
    # TODO make other userful locals
    def new_random(cls, is_male: bool = True, local: str = "PL"):
        return Person.pl_random(is_male)


    @classmethod
    # TODO test and finish
    def pl_random(cls, is_male: bool = None):
        is_male = is_male or u.true_or_false()

        name = random.choice(mock.pl_male_names) if is_male else random.choice(mock.pl_female_names)
        surname = random.choice(mock.pl_surnames) if is_male else create_pl_female_surname()
        return Person(name, surname)

