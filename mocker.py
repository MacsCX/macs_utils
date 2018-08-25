from mock import *
import random
from person import Person

# TODO oddzielna metoda na wczytanie pliku (walidacja, czy to jest JSON)
# TODO oddzielna metoda do parsowania obiektu

example = [{"$repeat": 5},
           {
               "id": "counter",
               "name": "person.name",
               "surname": "person.surname",
               "email": "person.email",
               "avatar": "avatar_url()",
               "weird": [{"$repeat": 12}, "15"]
           }]

print(isinstance(example, list))
# example = "$Uszanowanko!\n Hehe"

example2 = [{"$repeat": 1}, "person.name", "person.surname", "person.email"]
example3 = [{"$repeat": 12}, "counter"]


# class looper():
#     def __init__(self, repeat: int, counter: int = 0):
#         self.repeat = repeat,
#         self.counter = counter


def _parse_element(element, counter: int = 0, person: Person = None):
    start_counter = counter
    person = person or Person.pl_random()

    #### string
    if isinstance(element, str):
        if element[0] == "$":
            # TODO implementacja obsługi modeli np. $my_model
            result = "This is a model example, TO DO!"
        else:
            try:
                result = eval(element)
            except (NameError, SyntaxError) as e:
                result = element

    #### list
    elif isinstance(element, list):
        result = []
        try:
            # if $repeat is present
            if isinstance(element[0], dict) and "$repeat" in element[0].keys():
                repeat = element[0]["$repeat"]
                counter = start_counter

                for _ in range(repeat):
                    result += _parse_element(element[1:])

            else:
                for x in element:
                    result.append(x, counter)
        except IndexError:
            result = []


    #### dictionary
    elif isinstance(element, dict):

        result = {}
        for key in element.keys():
            result[key] = _parse_element(element[key], counter, person)

    #### integer or float
    elif u.is_number(element):
        result = element

    else:
        result = "dupa"

    return result


print(_parse_element(example2))
