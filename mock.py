import utils as u
from person import Person
import os
import random

mock_data_path = os.path.join(u.get_dir_abs_path(__file__), "mock_data")


def read_mock_txt(file_name: str):
    return u.read_csv_as_array(os.path.join(mock_data_path, file_name), has_one_column=True)


pl_male_names = read_mock_txt("PL-male_names.txt")
pl_female_names = read_mock_txt("PL-female_names.txt")
pl_surnames = read_mock_txt("PL-surnames.txt")
domains = read_mock_txt("domains.txt")

names = pl_male_names + pl_female_names
surnames = pl_surnames


def create_email(name: str = "", surname: str = "",
                 domain: str = "",
                 user: Person = None):
    # TODO make description for doc
    # TODO finish

    if user is None:
        user = Person.new_random(is_male=u.true_or_false())
        name = user.name
        surname = user.surname

    if domain == "":
        domain = random.choice(domains)

    name = u.simplify_string(name).lower()
    surname = u.simplify_string(surname).lower()

    return "{0}.{1}@{2}".format(name, surname, domain)
