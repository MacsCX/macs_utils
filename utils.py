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


def is_array(obj: object):
    """check if object type is list, tuple or set"""
    return type(obj) is list or type(obj) is set or type(obj) is tuple


def is_number(obj: object):
    """check if object type is integer or float"""
    return type(obj) is int or type(obj) is float


#### CSV and TXT

def read_txt_as_string(file_path: str, split_lines: bool = True):
    result_string = ""
    with open(file_path) as file:
        for line in file:
            line = line if split_lines else " ".join(line.split("\n"))
            result_string += line
    return result_string


def read_csv_as_array(file_path: str, start_index: int = 0, delimiter: str = "\t", has_one_column: bool = False):
    """
    :param file_path:
    :param start_index: 
    :param delimiter:
    :param has_one_column:
    :return: CSV parsed to an array 
    """
    file_path = os.path.abspath(file_path)
    parsed_data = []
    with open(file_path) as file:
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


def save_to_csv(content: object, output_path: str, delimiter: str = "", write_mode: str = "w"):
    """
    Save content to csv/txt file
    :param content: string or any type of array. Array's elements will be saved in separate lines.
    :param output_path:
    :param delimiter:
    :param write_mode: "w" - write, "a" - append
    :return:
    """
    all_content_to_write = ""
    if is_array(content):
        for element in content:
            if is_array(element):
                element = [str(x) for x in element]  # convert array's elements to strings
                all_content_to_write += delimiter.join(element) + "\n"
            else:
                all_content_to_write += str(element)
    else:
        all_content_to_write = str(content)

    with open(output_path, write_mode) as file:
        file.write(all_content_to_write)


#### JSON

def read_json_file(file_path: str):
    """
    :param file_path:
    :return: JSON file content parsed to dict
    """
    with open(file_path) as file:
        json_dict = json.load(file)

    return json_dict


def save_to_json(dictionary: dict, output_path: str):
    """
    Save dictionary to JSON file
    :param dictionary:
    :param output_path:
    """
    with open(output_path, "w") as file:
        json.dump(dictionary, file, indent=2)


#### DATES & TIME

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

    if not is_number(unixtimestamp):
        raise TypeError("Provided timestamp is not integer/float!")

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


def from_iso8601_to_datetime(dt: str):
    return datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%f%z")


def from_datetime_to_iso8601(dt: datetime):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")


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


def simplify_string(string: str):
    """
    Simplify string by removing spaces, special chars and normalizing polish chars
    :param string:
    :return:
    """
    return remove_spaces(
        remove_special_chars(
            normalize_polish_chars(string)
        )
    )


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
