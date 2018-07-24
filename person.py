from utils import *
import os, random

mock_data_path = os.path.join(get_dir_abs_path(__file__), "mock_data")
read_mock = lambda file_name: read_csv_as_array(os.path.join(mock_data_path, file_name), has_one_column=True)
pl_male_names = read_mock("PL-male_names.txt")
pl_female_names = read_mock("PL-female_names.txt")
pl_surnames = read_mock("PL-surnames.txt")


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
