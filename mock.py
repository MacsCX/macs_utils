import utils as u
from person import Person
import os
import random
from random import randint

mock_data_path = os.path.join(u.get_dir_abs_path(__file__), "mock_data")


def read_mock_txt(file_name: str) -> list:
    return u.read_csv_as_array(os.path.join(mock_data_path, file_name), has_one_column=True)


en_color_names = read_mock_txt("EN-color_names.txt")
en_animals = read_mock_txt("EN-animals.txt")
pl_male_names = read_mock_txt("PL-male_names.txt")
pl_female_names = read_mock_txt("PL-female_names.txt")
pl_surnames = read_mock_txt("PL-surnames.txt")
pl_car_plate_codes = read_mock_txt("PL-car_plate_codes.txt")
domains = read_mock_txt("domains.txt")
tech_terms = read_mock_txt("tech_terms.txt")

names = pl_male_names + pl_female_names
surnames = pl_surnames

company_name_suffixes = ["Solutions", "LTD", "Labs", "Inc.", "Company", "Sp. z o.o.", "GmbH", "Technologies",
                         "Dynamics", "Partners", "Holdings", "Development"]


def create_email(name: str = None, surname: str = None,
                 domain: str = None):
    """
    Create email using name and surname. If data is empty, random pseudo will be used.
    :param name:
    :param surname:
    :param domain: for example qooqle.com
    :return: email, for example jan.kowalski85@qmail.com or blue.dog99@qmail.com
    """

    # if name and surname are None, script create email with pseudo, f.e. "blue.dog12@qmail.com"
    name = name or random.choice(en_color_names)
    surname = surname or random.choice(en_animals)

    if domain is None:
        domain = random.choice(domains)

    name = u.simplify_string(name).lower()
    surname = u.simplify_string(surname).lower() + str(randint(1, 100))

    return "{0}.{1}@{2}".format(name, surname, domain)


def create_business_name():
    """create random business name using technical terms """

    return "%s %s" % (random.choice(tech_terms), random.choice(company_name_suffixes))


def create_pl_car_plate():
    """create random PL car plate, for example KRA 99ABC"""

    car_plate_code = random.choice(pl_car_plate_codes)

    return "{0} {1}{2}{3}{4}{5}".format(car_plate_code,
                                        randint(0, 9),
                                        randint(0, 9),
                                        chr(randint(65, 90)),
                                        chr(randint(65, 90)),
                                        chr(randint(65, 90))
                                        )


def get_adorable_avatar_url(size: int = 200, file_format: str = "jpg"):
    """
    Get url of Adorable avatar (square random funny face)
    :param size: size in px
    :param file_format: jpg/png/gif
    :return:
    """
    return "https://api.adorable.io/avatars/%d/%d.%s" % (size, randint(1, 100000), file_format)


def get_robohash_avatar_url(width: int = 200, height: int = 200):
    """
    Get url of Robohash PNG-only avatar (funny robot with alpha channel)
    :param width: px
    :param height: px
    :return:
    """
    return "https://robohash.org/%d.png?size%dx%d" % (randint(1, 100000), width, height)


def get_avatar_url(size: int = 200):
    """
    Return proper, improper or empty image url
    :param size: px
    :return:
    """
    return random.choice([get_adorable_avatar_url(size),
                          get_robohash_avatar_url(size, size),
                          "https://invalid.url.cs",
                          ""])
