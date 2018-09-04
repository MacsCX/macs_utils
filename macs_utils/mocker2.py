from macs_utils import mock
from macs_utils.person import Person
from macs_utils import utils as u
from datetime import datetime, timedelta
import random


def find_setting(obj: object, setting: str):
    # setting template - {"setting_name": "setting_value"}

    if isinstance(obj, list):
        for element in obj:
            if isinstance(element, dict) and setting in element.keys():
                obj.remove(element)
                return element[setting]

    elif isinstance(obj, dict):
        if setting in obj.keys():
            return obj[setting]

    else:
        return None


def time_delta_setting(obj: object):
    # TODO make one method instead 2 (this and period_length_setting)
    catched_value = find_setting(obj, "$time_delta")  # for example: 'hours=12' as string
    if catched_value is None:
        return None
    time_delta = eval(f"timedelta({catched_value})")
    return time_delta


def period_length_setting(obj: object):
    catched_value = find_setting(obj, "$period_length")  # for example: 'hours=12' as string
    if catched_value is None:
        return None
    time_delta = eval(f"timedelta({catched_value})")
    return time_delta


def _parse_element(element, counter: int = 12, person: Person = None, start_date: datetime = None,
                   time_delta: timedelta = None, period_length: timedelta = None):
    # TODO kwargs
    start_counter = counter
    person = person or Person.pl_random()
    start_date = start_date or u.round_datetime(datetime.now(), accuracy_hours=1)
    time_delta = time_delta or timedelta(hours=24)
    period_length = period_length or timedelta(hours=1)

    end_date = start_date + period_length

    #### string
    if isinstance(element, str):

        if element[0] == "$" and element != "$repeat":

            if element[-5:] == ".json":
                result = _parse_element(u.read_json_file(element[1:]), counter=counter, start_date=start_date, time_delta=time_delta,
                                       period_length=period_length)

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

            repeat = find_setting(element, "$repeat")
            start_date = find_setting(element, "$start_date") or start_date
            time_delta = time_delta_setting(element) or time_delta
            period_length = period_length_setting(element) or period_length

            if repeat is not None:
                for _ in range(repeat):
                    result += [
                        _parse_element(element, counter=counter, start_date=start_date, time_delta=time_delta,
                                       period_length=period_length)]
                    counter += 1
                    start_date += time_delta
            else:
                for x in element:
                    result.append(_parse_element(x, counter=counter, start_date=start_date, time_delta=time_delta,
                                                 period_length=period_length))
                    counter += 1

        except IndexError:
            result = []


    #### dictionary
    elif isinstance(element, dict):

        result = {}
        for key in element.keys():
            print(counter)
            result[key] = _parse_element(element[key], person=person, counter=counter, start_date=start_date,
                                         time_delta=time_delta,
                                         period_length=period_length)

    #### integer or float
    elif u.is_number(element):
        result = element

    else:
        result = None

    if not u.is_number(result) and not u.is_array(result) and not isinstance(result, str) and not isinstance(result,
                                                                                                             dict) and not isinstance(
        result, bool):
        result = str(result)

    return result

# test1 = [
#     {"$repeat": 5},
#     {"$time_delta": "hours=12"},
#     {
#         "name": "$person.name",
#         "surname": "$person.surname",
#         "dateRange":
#             {"date": "$start_date",
#              "end_date": "$end_date"}
#     }
# ]
#
# test2 = [
#     {"$repeat": 5},
#     {"$time_delta": "hours=12"},
#     "$start_date"
# ]
#
# test_result = _parse_element(test1)
# print(test_result)
#
# u.save_to_json(test_result, "test.json")
