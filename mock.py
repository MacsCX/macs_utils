import utils as u
import os
import random
from random import randint

_mock_data_path = os.path.join(u.get_dir_abs_path(__file__), "mock_data")
_strings_dir_path = os.path.join(_mock_data_path, "long_strings")
_string_names = [file_name.split(".")[0] for file_name in os.listdir(_strings_dir_path)]

# reading long strings from TXT files ("mock_data/long_strings/")

_long_strings = {}

for string_name in _string_names:
    _long_strings[string_name] = u.read_txt_as_string("{0}/{1}.txt".format(_strings_dir_path, string_name))


def _read_mock_txt(file_name: str) -> list:
    return u.read_csv_as_array(os.path.join(_mock_data_path, file_name), has_one_column=True)


# In directory mock_data/long_strings you may find long strings, for example "Lorem ipsum"
# or vehicle's description from Wiki

en_color_names = _read_mock_txt("EN-color_names.txt")
en_animals = _read_mock_txt("EN-animals.txt")
pl_male_names = _read_mock_txt("PL-male_names.txt")
pl_female_names = _read_mock_txt("PL-female_names.txt")
pl_surnames = _read_mock_txt("PL-surnames.txt")
pl_car_plate_codes = _read_mock_txt("PL-car_plate_codes.txt")
domains = _read_mock_txt("domains.txt")
tech_terms = _read_mock_txt("tech_terms.txt")

names = pl_male_names + pl_female_names
surnames = pl_surnames

company_name_suffixes = ["Solutions", "LTD", "Labs", "Inc.", "Company", "Sp. z o.o.", "GmbH", "Technologies",
                         "Dynamics", "Partners", "Holdings", "Development"]


def email(name: str = None, surname: str = None,
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


def business_name():
    """create random business name using technical terms """

    return "%s %s" % (random.choice(tech_terms), random.choice(company_name_suffixes))


def pl_car_plate():
    """create random PL car plate, for example KRA 99ABC"""

    car_plate_code = random.choice(pl_car_plate_codes)

    return "{0} {1}{2}{3}{4}{5}".format(car_plate_code,
                                        randint(0, 9),
                                        randint(0, 9),
                                        chr(randint(65, 90)),
                                        chr(randint(65, 90)),
                                        chr(randint(65, 90))
                                        )


def adorable_avatar_url(size: int = 200, file_format: str = "jpg"):
    """
    Get url of Adorable avatar (square random funny face)
    :param size: size in px
    :param file_format: jpg/png/gif
    :return:
    """
    return "https://api.adorable.io/avatars/{0}/{1}.{2}".format(size, randint(1, 100000), file_format)


def robohash_avatar_url(width: int = 200, height: int = 200):
    """
    Get url of Robohash PNG-only avatar (funny robot with alpha channel)
    :param width: px
    :param height: px
    :return:
    """
    return "https://robohash.org/{0}.png?size{1}x{2}".format(randint(1, 100000), width, height)


def avatar_url(size: int = 200):
    """
    Return proper, improper or empty image url
    :param size: px
    :return:
    """
    return random.choice([adorable_avatar_url(size),
                          robohash_avatar_url(size, size),
                          "https://invalid.url.cs",
                          ""])


def dummy_image_url(width: int = 200, height: int = 200, file_format: str = "jpg"):
    """
    Get url to simple rectangular image
    :param width: px
    :param height: px
    :param file_format: jpg/png/git/bmp
    :return:
    """
    font_color = "".join([hex(randint(0, 255))[2:] for _ in range(3)])
    background_color = "".join([hex(randint(0, 255))[2:] for _ in range(3)])
    return "https://dummyimage.com/{0}x{1}.{2}/{3}/{4}".format(width,
                                                               height,
                                                               file_format,
                                                               font_color,
                                                               background_color)


def long_string(*args):
    """
    Return long string, (Lorem ipsum or other)
    :param args: file name (without '.txt'),
    :return:
    """

    string_name = random.choice(_string_names)

    for x in args:
        if x in _string_names:
            string_name = x
            break

    string = _long_strings[string_name]

    if "one_line" in args:
        string = " ".join(string.split("\n"))

    return string

