from utils import *
import os, random

mock_data_path = os.path.join(get_dir_abs_path(__file__), "mock_data")
read_mock = lambda file_name: read_csv_as_array(os.path.join(mock_data_path, file_name), has_one_column=True)
pl_male_names = read_mock("PL-male_names.txt")
pl_female_names = read_mock("PL-female_names.txt")
pl_surnames = read_mock("PL-surnames.txt")

### FINISH!
def create_pl_female_surname(surname: str = "", second_surname: str = ""):
    """
    Create polish female. If input is empty, you'll get random polish surname as result
    :param surname:
    :return:
    """

    def feminize(surname):
        if surname[:-1] == ("i" or "y"):
            surname = replace_char(surname, -1, "a")

        return surname
    ### Just for now...
    return surname


class Person():
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return "%s %s" % (self.name, self.surname)

    def __str__(self):
        return repr(self)
