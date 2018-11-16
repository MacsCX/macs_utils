from macs_utils import utils as u
import os
import random
from random import randint

_mock_data_path = os.path.join(u.get_dir_abs_path(__file__), "mock_data")
_strings_dir_path = os.path.join(_mock_data_path, "long_strings")
_string_names = [file_name.split(".")[0] for file_name in os.listdir(_strings_dir_path)]

# reading long strings from TXT files ("mock_data/long_strings/")

_long_strings = {}

# In directory mock_data/long_strings you may find long strings f.e. "Lorem ipsum", etc.
for string_name in _string_names:
    _long_strings[string_name] = u.read_txt_as_string("{0}/{1}.txt".format(_strings_dir_path, string_name))


def _read_mock_txt(file_name: str) -> list:
    return u.read_csv_as_array(os.path.join(_mock_data_path, file_name), has_one_column=True)


en_color_names = _read_mock_txt("EN-color_names.txt")
en_animals = _read_mock_txt("EN-animals.txt")
pl_male_names = _read_mock_txt("PL-male_names.txt")
pl_female_names = _read_mock_txt("PL-female_names.txt")
pl_surnames = _read_mock_txt("PL-surnames.txt")
pl_car_plate_codes = _read_mock_txt("PL-car_plate_codes.txt")
pl_cities = _read_mock_txt("PL-cities.txt")
domains = _read_mock_txt("domains.txt")
tech_terms = _read_mock_txt("tech_terms.txt")

names = pl_male_names + pl_female_names
surnames = pl_surnames

company_name_suffixes = ["Solutions", "LTD", "Labs", "Inc.", "Company", "Sp. z o.o.", "GmbH", "Technologies",
                         "Dynamics", "Partners", "Holdings", "Development"]


def email(name: str = None, surname: str = None, domain: str = None):
    """create email using name and surname. If data is empty, random pseudo will be used"""

    name = name or random.choice(en_color_names)
    surname = surname or random.choice(en_animals)

    if domain is None:
        domain = random.choice(domains)

    name = u.simplify_string(name).lower()
    surname = u.simplify_string(surname).lower() + str(randint(1, 100))

    return "{0}.{1}@{2}".format(name, surname, domain)


def business_name():
    """create random business name using technical terms"""

    return "%s %s" % (random.choice(tech_terms), random.choice(company_name_suffixes))


def pl_car_plate():
    """create random PL car plate, for example KRA 99ABC"""

    car_plate_code = random.choice(pl_car_plate_codes)

    car_plate_string = str(randint(10, 99))
    car_plate_string += "".join([chr(randint(65, 90)) for x in range(3)])

    return "%s %s" % (car_plate_code, car_plate_string)


def nickname():
    """create random nickname using EN colors and animal names"""
    color = random.choice(en_color_names)
    animal = random.choice(en_animals)

    if u.true_or_false():
        return f"{color.capitalize()}{animal.capitalize()}{randint(0,100)}"
    else:
        return f"{color}_{animal}{randint(0,100)}"


def adorable_avatar_url(size: int = 200, file_format: str = "jpg"):
    """get url of Adorable avatar (square random funny face)"""
    return "https://api.adorable.io/avatars/{0}/{1}.{2}".format(size, randint(1, 100000), file_format)


def robohash_avatar_url(width: int = 200, height: int = 200):
    """get url of Robohash PNG-only avatar (funny robot with alpha channel)"""
    return "https://robohash.org/{0}.png?size{1}x{2}".format(randint(1, 100000), width, height)


def picsum_url(width: int = 200, height: int = 200, is_random: bool = True):
    """get url of Lorem Picsum image"""
    url = f"https://picsum.photos/{width}/{height}"

    if is_random:
        url += "/?image=" + str(randint(1, 1084))

    return url


def avatar_url(size: int = 200):
    """return proper, improper or empty image url"""
    return random.choice([adorable_avatar_url(size),
                          robohash_avatar_url(size, size),
                          "https://invalid.url.cs",
                          ""])


def dummy_image_url(width: int = 200, height: int = 200, file_format: str = "jpg"):
    """get url to simple rectangular jpg/png/git/bmp image"""
    font_color = "".join([hex(randint(0, 255))[2:] for _ in range(3)])
    background_color = "".join([hex(randint(0, 255))[2:] for _ in range(3)])
    return "https://dummyimage.com/{0}x{1}.{2}/{3}/{4}".format(width,
                                                               height,
                                                               file_format,
                                                               font_color,
                                                               background_color)


def long_string(*args: object) -> str:
    """
    return long string, (Lorem ipsum or other)
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
