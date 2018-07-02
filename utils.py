"""
This module contains useful methods. Enjoy!
"""
import json
import os
import random
from random import randint
import datetime
import time
import calendar

polish_chars = {"ą": "a",
                "ć": "c",
                "ę": "e",
                "ł": "l",
                "ń": "n",
                "ó": "o",
                "ś": "s",
                "ż": "z",
                "ź": "z"}


#### CSV

def read_csv_as_array(csv_file_path: str, start_index: int = 0, delimiter: str = "\t"):
    """
    :param csv_file_path: 
    :param start_index: 
    :param delimiter: 
    :return: CSV parsed to an array 
    """
    csv_file_path = os.path.abspath(csv_file_path)
    parsed_data = []
    with open(csv_file_path) as file:
        for line in file:
            line = line.rstrip("\n")
            line = line.split(delimiter)  # line is transformed into array
            parsed_data.append(line)

    return parsed_data[start_index:]


def is_csv_correct(csv_array: list):
    """
    Check if CSV's lines has the same number of columns
    :param csv_array: CSV parsed to an array
    :return: Boolean
    """
    for i in range(len(csv_array) - 1):
        if len(csv_array[i]) != len(csv_array[i + 1]):
            return False

    return True


#### JSON

def read_json_file(json_file_path: str):
    """
    :param json_file_path:
    :return: JSON file content parsed to dict
    """
    with open(json_file_path) as file:
        json_dict = json.load(file)

    return json_dict


def save_json_to_file(dictionary: dict, file_path: str):
    """
    Save dictionary to JSON file
    :param dictionary:
    :param file_path:
    """
    with open(file_path, "w") as file:
        json.dump(dictionary, file, indent=2)


#### DATES
def datetime_to_unixtimestamp(given_datetime: datetime):
    """
    Convert datetime object to unix timestamp
    :param given_datetime: datetime object
    :return: unix timestamp
    """
    return int(time.mktime(given_datetime.timetuple()))


def round_unixtimestamp_to_minutes(unix_timestamp, min_to_round: int = 15):
    modulo = unix_timestamp % (min_to_round * 60)
    if modulo >= (min_to_round * 60 / 2):
        unix_timestamp += min_to_round * 60 - modulo
    else:
        unix_timestamp -= modulo

    return unix_timestamp


def round_datetime_to_minutes(given_datetime, min_to_round: int = 15):
    unix_dt = datetime_to_unixtimestamp(given_datetime)
    rounded_unix_dt = round_unixtimestamp_to_minutes(unix_dt, min_to_round)

    return unixtimestamp_to_datetime(rounded_unix_dt)


def datetime_to_string(given_datetime: datetime, day_name_length: int):
    day_name = calendar.day_name[given_datetime.weekday()][0:day_name_length]
    return "{} {}".format(day_name,
                          str(given_datetime)[:22])


def unixtimestamp_to_datetime(unix_timestamp):
    return datetime.datetime.fromtimestamp(int(unix_timestamp))


def datify_elements(array: list, start_date_key: str, end_date_key: str, date_range_key: str,
                    should_insert_to_name: bool, name_key: str, delete_chars_from_name: int = -9,
                    start_x_days_before: int = 30, interval_hours=6, is_first_element_multidate: bool = True):
    dt = datetime.datetime.now() - datetime.timedelta(days=start_x_days_before)
    dt -= datetime.timedelta(hours=6)
    dt = round_datetime_to_minutes(dt, 15)
    for element in array:

        start_date = datetime_to_unixtimestamp(dt)
        end_date = start_date + random.randint(1, 12) * 900  # 900 = 15 min

        if array.index(element) == 0 and is_first_element_multidate:
            end_date = end_date + 172800  # first element will be multidate

        if date_range_key == "":
            element[start_date_key] = start_date
            element[end_date_key] = end_date
        else:
            element[date_range_key][start_date_key] = start_date
            element[date_range_key][end_date_key] = end_date

        if should_insert_to_name:
            element[name_key] = datetime_to_string(dt, 3)[:delete_chars_from_name] + " " + element[name_key]

        dt = dt + datetime.timedelta(hours=interval_hours)

    return array


#### STRINGS

def change_char(string: str, char_index: int, new_char: str):
    string = list(string)
    string[char_index] = new_char

    return "".join(string)


def replace_polish_chars_with_ascii(string: str):
    string = list(string)
    result = []

    for character in string:
        if character.lower() in polish_chars.keys():
            if character.isupper():
                character = polish_chars[character.lower()].upper()
            else:
                character = polish_chars[character]
        result.append(character)

    return "".join(result)


def remove_special_chars_from_string(string: str):
    string = list(string)
    result = []

    for character in string:
        if ord(character) in range(0, 65):
            continue
        result.append(character)

    return "".join(result)


def remove_spaces_from_string(string: str):
    string = list(string)
    result = []

    for character in string:
        if character == " " or character == "\t":
            continue
        result.append(character)

    return "".join(result)


#### OTHER

def true_or_false():
    return random.choice([True, False])


def create_subarray(array, can_be_empty):
    subarray = []

    for element in array:
        if true_or_false():
            subarray.append(element)

    if can_be_empty == False and len(subarray) == 0:
        subarray.append(random.choice(array))
    return subarray


def make_arrays_element_dominating(array: list, element_index: int,
                                   number_of_clones: int):  # it clones element multiple times to change ratio in array

    new_array = array.copy()

    for i in range(0, number_of_clones):
        new_array.append(array[element_index])

    return new_array


def make_array_from_dict_values(dictionary: dict, key: str):
    array = []
    for element in dictionary:
        array.append(element[key])

    return array


def print_array(array: list):
    for element in array:
        print(str(element))
