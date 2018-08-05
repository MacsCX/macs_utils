"""
This module contains useful methods. Enjoy!
"""
import json
import os
import random
import re
from random import randint
from datetime import datetime

polish_chars = {"ą": "a",
                "ć": "c",
                "ę": "e",
                "ł": "l",
                "ń": "n",
                "ó": "o",
                "ś": "s",
                "ż": "z",
                "ź": "z"}


#### OBJECTS

def get_attributes(ob: object, *args) -> tuple:
    '''
    return attributes' values as a tuple
    :param ob: object
    :param args: attributes' names as strings
    :return:
    '''
    return tuple(getattr(ob, attribute) for attribute in args)


def get_key_values(dictionary: dict, *args):
    '''
    return key values as a tuple
    :param dictionary:
    :param args: keys' names as strings
    :return:
    '''
    return tuple(dictionary[key] for key in args)


#### CSV

def read_csv_as_array(csv_file_path: str, start_index: int = 0, delimiter: str = "\t", has_one_column: bool = False):
    """
    :param csv_file_path: 
    :param start_index: 
    :param delimiter:
    :param has_one_column:
    :return: CSV parsed to an array 
    """
    csv_file_path = os.path.abspath(csv_file_path)
    parsed_data = []
    with open(csv_file_path) as file:
        for line in file:
            line = line.rstrip("\n")
            if not has_one_column:
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

# TO DELETE
# def datetime_to_unixtimestamp(given_datetime: datetime):
#     """
#     Convert datetime object to unix timestamp
#     :param given_datetime: datetime object
#     :return: unix timestamp
#     """
#     return int(time.mktime(given_datetime.timetuple()))


def round_unixtimestamp(unixtimestamp, accuracy_sec: int = 0, accuracy_min: int = 0, accuracy_hours: int = 0):
    """
    Round unixtimestamp with given accuracy
    :param unixtimestamp: type - float or integer
    :param accuracy_min:
    :param accuracy_hours:
    :param accuracy_sec:
    :return:
    """

    accuracy = accuracy_hours * 3600 + accuracy_min * 60 + accuracy_sec

    if (isinstance(unixtimestamp, float) and isinstance(unixtimestamp, float)) == False:
        raise TypeError("Provided timestamp is not integer or float!")

    modulo = unixtimestamp % accuracy
    if modulo >= (accuracy / 2):
        unixtimestamp += accuracy - modulo
    else:
        unixtimestamp -= modulo

    return unixtimestamp


def round_datetime(given_datetime: datetime, accuracy_sec: int = 0, accuracy_min: int = 0, accuracy_hours: int = 0):
    """
    Round datetime object with given accuracy
    :param given_datetime: datetime object (datetime module)
    :param accuracy_sec:
    :param accuracy_min:
    :param accuracy_hours:
    :return:
    """
    unixtimestamp = given_datetime.timestamp()
    return given_datetime.fromtimestamp(
        round_unixtimestamp(unixtimestamp, accuracy_sec, accuracy_min, accuracy_hours)
    )


def from_iso8601_to_datetime(date: str):
    pattern = r"[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]T[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]\+[0-9][0-9]\:[0-9][0-9]"
    if re.match(pattern, date):
        date = [int(x) for x in re.split("\-|T|\+|\:", date)]
        date[3] += date[6]
        date[4] += date[7]
        dt_date = datetime(*date[:6])
        return dt_date
    else:
        raise ValueError("Provided string does not match ISO 8601 pattern")


#### STRINGS

def replace_char(string: str, char_index: int, new_char: str):
    """
    Replace chars in string
    :rtype: object
    :param string:
    :param char_index:
    :param new_char:
    :return:
    """
    string = list(string)
    string[char_index] = new_char

    return "".join(string)


def normalize_polish_chars(string: str):
    """
    Change polish chars to ASCII chars
    unicode.normalize doesn't work well, because of "Ł" and "ł" ;)
    :param string:
    :return:
    """
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


def remove_special_chars(string: str):
    """
    Remove special chars from string
    :param string:
    :return:
    """
    string = list(string)
    result = []

    for character in string:
        if ord(character) in range(0, 65):
            continue
        result.append(character)

    return "".join(result)


def remove_spaces(string: str):
    """
    Remove spaces, tabs and "\n" from string
    :param string:
    :return:
    """

    return "".join(string.split())


#### OTHER

def true_or_false(true_weight: int = 1, false_weight: int = 1):
    """
    Draw a boolen with various degrees of probability
    :param true_weight:
    :param false_weight:
    :return: True or False
    """
    return random.choice([True] * true_weight + [False] * false_weight)


def create_random_subarray(array: list, exact_length: int = 0, min_length: int = 0, max_length: int = 0):
    """
    Create subarray
    :param array: 1-D array
    :param exact_length: for subarray with exact length
    :param min_length:
    :param max_length:
    :return: 1-D subarray
    """
    subarray = []
    array_copy = array.copy()

    if exact_length == 0:

        if max_length == 0:
            max_length = len(array)

        exact_length = randint(min_length, max_length)

    elif exact_length > len(array):
        raise ValueError("Exact subarray's length is bigger than provided array's length")

    for counter in range(exact_length):
        subarray.append(
            array_copy.pop(randint(0, len(array_copy) - 1))
        )

    return subarray


def get_dir_abs_path(file_name: str):
    """
    Return absolute path to file's directory
    :param file_name:
    :return:
    """
    return os.path.abspath(os.path.dirname(file_name))


abs_path = lambda x: os.path.abspath(x)
