# -*- coding: utf-8 -*-

import sys_utils as su
import random
from random import randint
import os
import datetime

mock_data_dir_path = os.path.abspath(os.path.dirname(__file__)) + "/mock_data/"


def read_mock_txt(file_name: str):
    return su.read_one_column_txt(mock_data_dir_path + file_name, 0)


def read_mock_json(file_name: str):
    return su.read_json_file(mock_data_dir_path + file_name)


names = read_mock_txt("names.txt")
polish_male_names = read_mock_txt("polish_male_names.txt")
polish_female_names = read_mock_txt("polish_female_names.txt")
polish_surnames = read_mock_txt("polish_surnames.txt")
surnames = read_mock_txt("surnames.txt")
room_names = read_mock_txt("room_names.txt")
event_names = read_mock_txt("event_names.txt")
weird_strings = read_mock_txt("weird_strings.txt")
mickiewicz_invocation = read_mock_txt("mickiewicz.txt")
polish_cities = read_mock_txt("polish_cities.txt")
polish_streets = read_mock_txt("polish_streets.txt")
business_names = read_mock_txt("business_names.txt")
kobuz = " ".join(read_mock_txt("kobuz.txt"))
polish_car_plate_codes = [line.split(" - ") for line in read_mock_txt("polish_car_plate_codes.txt")]


####### EVENTS, PLACES, ETC.

def get_event_name():
    return random.choice(event_names)


def get_business_name():
    business_name = random.choice(business_names)

    if su.true_or_false():
        owner = create_polish_user()
        business_name = "{} {} {}".format(business_name,
                                          owner["name"],
                                          owner["surname"]
                                          )
    else:
        business_name = "{} {}".format(business_name,
                                       random.choice(["Sp. z o.o.", "S.A.", "Inc.", "GmbH", "Sp. Komandytowa"])
                                       )

    return business_name


def create_room_name():
    return "{} {}".format(
        random.choice(room_names + polish_cities),
        random.randint(1, 10000)
    )


def get_polish_street(hasLongPrefix: bool, hasBuildingNumber: bool, hasFlatNumber: bool):
    prefix = random.choice(
        su.make_arrays_element_dominating(["ulica", "aleja"], 0, 6)
    )

    if hasLongPrefix == False:
        prefix = prefix[:2] + "."

    street = "{} {}".format(prefix,
                            random.choice(polish_streets)
                            )

    if hasBuildingNumber:
        building_number = str(randint(1, 150)) + random.choice(
            su.make_arrays_element_dominating(["", "a", "b", "c", "d"], 0, 10)
        )
        if hasFlatNumber:
            building_number = "{}/{}".format(building_number,
                                             str(randint(1, 150))
                                             )
        street = street + " " + building_number

    return street


def get_polish_postal_code():
    return "{}-{}".format(str(randint(10, 99)),
                          str(randint(100, 999)))


###### PEOPLE

def get_name():
    return random.choice(names)


def get_surname():
    return random.choice(surnames)


def get_polish_single_surname_for_female():
    surname = random.choice(polish_surnames)
    if surname[-1:] == "i":
        surname = su.change_char(surname, -1, "a")

    return surname


def get_polish_double_surname_for_female():
    first_surname = get_polish_single_surname_for_female()

    while True:
        second_surname = get_polish_single_surname_for_female()
        if second_surname != first_surname:
            break

    return "{}-{}".format(first_surname, second_surname)


def get_polish_surname_for_female():
    isDouble = su.true_or_false()

    if isDouble:
        return get_polish_double_surname_for_female()
    else:
        return get_polish_single_surname_for_female()


def create_male_polish_user():
    return dict(name=random.choice(polish_male_names),
                surname=random.choice(polish_surnames))


def create_female_polish_user():
    name = random.choice(polish_female_names)
    surname = get_polish_surname_for_female()

    return dict(name=name, surname=surname)


def create_polish_user():
    isMale = su.true_or_false()

    if isMale:
        return create_male_polish_user()
    else:
        return create_female_polish_user()


def create_email_for_user(name: str, surname: str):
    name = su.replace_polish_chars_with_ascii(name).lower()
    name = su.remove_special_chars_from_string(name)
    surname = su.replace_polish_chars_with_ascii(surname).lower()
    surname = surname.split("-")[0]
    surname = su.remove_special_chars_from_string(surname)
    # if len(surname) > 10:
    #     surname = surname[:10]

    domain = "miquido.com"

    return "{}.{}{}@{}".format(name[0],
                               surname,
                               str(randint(70, 99)),
                               domain)


def create_random_polish_car_plate():
    """

    :return: car plate in format "LL NNLLL" (L- letter, N - number)
    """
    car_plate_code = random.choice(polish_car_plate_codes)[0]

    car_plate = "{0} {1}{2}{3}{4}{5}".format(car_plate_code,
                                             randint(0, 9),
                                             randint(0, 9),
                                             chr(randint(65, 90)),
                                             chr(randint(65, 90)),
                                             chr(randint(65, 90))
                                             )

    return car_plate


def get_random_car_model():
    car_list = read_mock_json("car-list.json")
    chosen_company = random.choice(car_list)
    brand = chosen_company["brand"]
    model = random.choice(chosen_company["models"])
    return "%s %s" % (brand, model)


def get_email():
    user = create_polish_user()
    return create_email_for_user(user["name"],
                                 user["surname"]
                                 )


### DATES & TIME

def get_unixtimestamp():
    dt = datetime.datetime.now() + datetime.timedelta(minutes=random.randint(-69120, 69120))
    return su.datetime_to_unixtimestamp(dt)

def convert_unixtimestamp_to_iso(unixtimestamp):
    return datetime.datetime.fromtimestamp(unixtimestamp).isoformat()



def get_adorable_avatar(size):
    url = "https://api.adorable.io/avatars"
    return "{}/{}/{}.jpg".format(url,
                                 str(size),
                                 str(random.randint(1, 100000))
                                 )


def get_one_line_invocation():  # generate 1-line invocation :)
    return " ".join(mickiewicz_invocation)


def weirdify_element(element):
    if type(element) is str:
        weird_strings_with_invocation = weird_strings
        weird_strings_with_invocation.append(get_one_line_invocation())
        element = random.choice(weird_strings_with_invocation)
    elif type(element) is float:
        element = random.uniform(1000000, 1000000000)
    elif type(element) is int:
        element = random.randint(1000000, 1000000000)
    elif type(element) is list:
        weirdified_array = []
        for element_of_sublist in element:
            element_of_sublist = weirdify_element(element_of_sublist)
            weirdified_array.append(element_of_sublist)
            element = weirdified_array
    elif type(element) is dict:
        for key in element.keys():
            element[key] = weirdify_element(element[key])
    else:
        element = element

    return element


def weirdify_dict(dictionary: dict, weirdify_all: bool = False):
    for key in dictionary.keys():
        if su.true_or_false() or weirdify_all:
            dictionary[key] = weirdify_element(dictionary[key])

    return dictionary


def weirdify_array(array: list, weirdify_all: bool = False):
    weirdified_array = []
    for element in array:
        if su.true_or_false():
            if type(element) is dict:
                element = weirdify_dict(element, weirdify_all)
            else:
                element = weirdify_element(element, weirdify_all)
        weirdified_array.append(element)

    return weirdified_array


def weirdify_json(json_data, weirdify_all: bool = False):
    if type(json_data) is dict:
        return weirdify_dict(json_data, weirdify_all)
    elif type(json_data) is list:
        return weirdify_array(json_data, weirdify_all)
    else:
        return json_data
