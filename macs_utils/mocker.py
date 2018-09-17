from macs_utils import mock
from macs_utils.person import Person
from macs_utils import utils as u
from datetime import datetime, timedelta
import random
import argparse

# TODO make some method provider

def _find_setting(obj: object, setting: str, *args):
    '''
    internal method for finding special settings like:
    repeat, time_delta, start_date, period_length
    :param obj:
    :param setting:
    :param args:
    :return:
    '''
    # setting template - {"setting_name": "setting_value"}
    result = None

    if "timedelta" in args:
        catched_value = _find_setting(obj, setting)  # for example: 'hours=12' as string
        if catched_value is None:
            result = None
        else:
            time_delta = eval(f"timedelta({catched_value})")
            result = time_delta

    elif isinstance(obj, list):
        for element in obj:
            if isinstance(element, dict) and setting in element.keys():
                obj.remove(element)
                result = element[setting]
                break

    elif isinstance(obj, dict):
        if setting in obj.keys():
            result = obj[setting]

    return result


def mock_element(element, counter: int = 0, start_date: datetime = None,
                 time_delta: timedelta = None, period_length: timedelta = None):
    '''
    Mock element
    :param element: string, dictionary, array or JSON file
    :param counter: counter's baseline value
    :param start_date: start date of events' sequence
    :param time_delta: interval between events' start dates
    :param period_length: event's length; parameters
    :return:
    '''

    start_date = start_date or u.round_datetime(datetime.now(), accuracy_hours=1)
    time_delta = time_delta or timedelta(hours=24)
    period_length = period_length or timedelta(hours=1)

    params = dict(locals().copy()) # this line copies keeps parameters
    del params["element"]

    start_counter = counter
    end_date = start_date + period_length
    person = Person.pl_random()

    #### string
    if isinstance(element, str):

        if element[0] == "$" and element != "$repeat":

            if element[-5:] == ".json": # that's for mocking models from JSON files
                result = mock_element(u.read_json_file(element[1:]), **params)

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

            repeat = _find_setting(element, "$repeat")
            start_date = _find_setting(element, "$start_date") or start_date
            time_delta = _find_setting(element, "$time_delta", "timedelta") or time_delta
            period_length = _find_setting(element, "$period_length", "timedelta") or period_length

            if repeat is not None:
                if isinstance(repeat, str):  # if $repeat is presented as tuple, f.e.: {"$repeat":"(1, 5)"}
                    repeat = eval(repeat)
                    mock_range = range(random.randint(*repeat))
                else:
                    mock_range = range(repeat)

                params_copy = params.copy()

                for _ in mock_range:
                    result += mock_element(element, **params_copy)
                    params_copy["counter"] += 1
                    params_copy["start_date"] += time_delta
            else:
                params_copy = params.copy()
                for x in element:
                    result.append(mock_element(x, **params_copy))
                    params_copy["counter"] += 1

        except IndexError:
            result = []


    #### dictionary
    elif isinstance(element, dict):

        result = {}
        for key in element.keys():
            result[key] = mock_element(element[key], **params)

    #### integer or float or boolean or None
    elif u.is_number(element) or isinstance(element, bool) or element is None:
        result = element

    else:
        result = str(element)

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path", help="path to model file")
    parser.add_argument("output_path", help="path to output file")
    parser.add_argument("--counter", "-c", action="store", type=int, help="counter's baseline value")

    args = parser.parse_args()
    counter = args.counter or 0
    model_path = args.model_path
    output_path = args.output_path

    model = u.read_json_file(model_path)

    u.save_to_json(mock_element(model, counter=counter), output_path)
