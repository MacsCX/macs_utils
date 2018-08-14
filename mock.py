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
tech_terms = read_mock_txt("tech_terms.txt")

names = pl_male_names + pl_female_names
surnames = pl_surnames

company_name_suffixes = ["Solutions", "LTD", "Labs", "Inc.", "Company", "Sp. z o.o.", "GmbH", "Technologies",
                         "Dynamics", "Partners", "Holdings", "Development"]


def create_email(name: str = None, surname: str = None,
                 domain: str = None,
                 user: Person = None):
    # TODO change random - instead of Person use f.e. "blue_dragon44@qmail.com"
    # TODO make description for doc
    # TODO finish

    if user is None:
        user = Person.new_random(is_male=u.true_or_false())
        name = user.name
        surname = user.surname

    if domain is None:
        domain = random.choice(domains)

    name = u.simplify_string(name).lower()
    surname = u.simplify_string(surname).lower()

    return "{0}.{1}@{2}".format(name, surname, domain)


def create_business_name(owner_name: str = None, owner_surname: str = None):
    # TODO test it!
    """create business name using technical terms and optionally owner's data"""
    if (owner_name is None) and (owner_surname is None):
        owner = ""
    else:
        owner = "%s %s " % (owner_name, owner_surname) # there is a space at the end!

    return "{0}{1} {2}".format(owner, random.choice(tech_terms), random.choice(company_name_suffixes))