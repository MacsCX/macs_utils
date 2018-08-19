from mock import *
import random

example = [
    {
        "$repeat": 5,
        "name": "random.choice(pl_male_names)",
        "surname": "random.choice(pl_surnames)",
        "avatar": "avatar_url()"
    }
]


def _parse_dict_pattern(pattern: dict):
    result = {}
    for key in pattern.keys():
        if pattern[key] is str:
            try:
                result[key] = eval(pattern[key])
            except NameError:
                result[key] = pattern[key]

        elif pattern[key] is dict:
            result[key] = _parse_dict_pattern(pattern[key])

        else:
            result[key] = pattern[key]

    return result


def _parse_json_object(obj: object):
    pattern = obj[0] if obj is list else obj

    if pattern is not dict:
        raise TypeError("Provided value cannot be read as JSON!")

    can_be_repeated = True if obj is list else False
    repeat = pattern.pop("$repeat") if "$repeat" in pattern.keys() else None

    if repeat is None and can_be_repeated:
        raise ValueError("No '$repeat' property")
