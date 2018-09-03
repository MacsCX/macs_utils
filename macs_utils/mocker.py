from macs_utils import mock
from macs_utils.person import Person
from macs_utils import utils as u

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

# example = "$Uszanowanko!\n Hehe"

example2 = [{"$repeat": 1}, "person.name", "person.surname", "person.email"]
example3 = [{"$repeat": 12}, "counter"]


def _parse_element(element, counter: int = 0, person: Person = None):
    start_counter = counter
    person = person or Person.pl_random()

    #### string
    if isinstance(element, str):

        if element[0] == "$" and element != "$repeat":

            if element[-5:] == ".json":
                result = _parse_element(u.read_json_file(element[1:]))

            else:
                try:
                    result = eval(element[1:])
                except (NameError, SyntaxError) as e:
                    result = element

        else:
            result = element

    #### list
    elif isinstance(element, list):
        result = []

        try:
            counter = start_counter

            # if $repeat is present
            if isinstance(element[0], dict) and "$repeat" in element[0].keys():
                repeat = element[0]["$repeat"]
                print(repeat)


                for _ in range(repeat):
                    # result = [_parse_element(x, counter) for x in element[1:]]
                    # counter += 1
                    result += _parse_element(element[1:], counter=counter)
                    counter += 1

            else:
                for x in element:
                    result.append(_parse_element(x))
                    counter += 1

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