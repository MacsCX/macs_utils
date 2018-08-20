from mock import *
import random

# TODO oddzielna metoda na wczytanie pliku (walidacja, czy to jest JSON)
# TODO oddzielna metoda do parsowania obiektu

example = {
        "$repeat": 5,
        "name": "random.choice(pl_male_names)",
        "surname": "random.choice(pl_surnames)",
        "avatar": "avatar_url()"
    }

# example = "$Uszanowanko!\n Hehe"

example = [{"$repeat": 1}, "random.choice(pl_surnames)"]

def _parse_element(element):
    if isinstance(element, str):
        if element[0] == "$":
            # TODO implementacja obsługi modeli np. $my_model
            result = "This is a model example, TO DO!"
        else:
            try:
                result = eval(element)
            # TODO jak to kurde zrobić do jednego excepta? :P
            except NameError:
                result = element
            except SyntaxError:
                result = element

    elif isinstance(element, list):
        result = []
        try:
            if isinstance(element[0], dict) and "$repeat" in element[0].keys():
                repeat = element[0]["$repeat"] - 1
                element.remove(element[0])
                for _ in range(repeat):
                    result += _parse_element(element)
        except IndexError:
            result = []

        for x in element:
            result.append(_parse_element(x))

    elif isinstance(element, dict):
        repeat = element.pop("$repeat") - 1 if "$repeat" in element.keys() else None

        if repeat is None:
            result = {}
            for key in element.keys():
                result[key] = _parse_element(element[key])
        else:
            result = []
            for _ in range(repeat):
                result.append(_parse_element(element))

    elif u.is_number(element):
        result = element

    else:
        result = "dupa"

    return result

print(_parse_element(example))


# def _parse_dict_pattern(pattern: dict):
#     result = {}
#     for key in pattern.keys():
#         if pattern[key] is str:
#             try:
#                 result[key] = eval(pattern[key])
#             except NameError:
#                 result[key] = pattern[key]
#
#         elif pattern[key] is dict:
#             result[key] = _parse_dict_pattern(pattern[key])
#
#         else:
#             result[key] = pattern[key]
#
#     return result
#
#
# def _parse_json_object(obj: object):
#     pattern = obj[0] if obj is list else obj
#
#     if pattern is not dict:
#         raise TypeError("Provided value cannot be read as JSON!")
#
#     can_be_repeated = True if obj is list else False
#     repeat = pattern.pop("$repeat") if "$repeat" in pattern.keys() else None
#
#     if repeat is None and can_be_repeated:
#         raise ValueError("No '$repeat' property")
