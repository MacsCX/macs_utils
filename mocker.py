from mock import *
import random

# TODO oddzielna metoda na wczytanie pliku (walidacja, czy to jest JSON)
# TODO oddzielna metoda do parsowania obiektu

example = [{"$repeat": 5},
{
    "id": "counter",
    "name": "random.choice(pl_male_names)",
    "surname": "random.choice(pl_surnames)",
    "avatar": "avatar_url()"
}]

print(isinstance(example, list))
# example = "$Uszanowanko!\n Hehe"

example2 = [{"$repeat": 1}, "random.choice(pl_surnames)"]

# class looper():
#     def __init__(self, repeat: int, counter: int = 0):
#         self.repeat = repeat,
#         self.counter = counter




def _parse_element(element, counter: int = 666):

    if isinstance(element, str):
        if element[0] == "$":
            # TODO implementacja obsługi modeli np. $my_model
            result = "This is a model example, TO DO!"
        # elif element == "counter":
        #     result = counter
        else:
            try:
                result = eval(element)
            except (NameError, SyntaxError) as e:
                result = element

    elif isinstance(element, list):
        result = []
        try:
            if isinstance(element[0], dict) and "$repeat" in element[0].keys():
                repeat = element[0]["$repeat"] - 1

                element.remove(element[0])
                for _ in range(repeat):
                    result += _parse_element(element, counter)
                    counter += 1

        except IndexError:
            result = []

        for x in element:
            result.append(_parse_element(x, counter))
            counter += 1

    elif isinstance(element, dict):
        repeat = element.pop("$repeat") - 1 if "$repeat" in element.keys() else None
        if repeat is None:
            result = {}
            for key in element.keys():
                result[key] = _parse_element(element[key])
        else:
            result = []
            for _ in range(repeat):
                result.append(_parse_element(element, counter))
                counter += 1
    elif u.is_number(element):
        result = element

    else:
        result = "dupa"

    return result


print(_parse_element(example))



