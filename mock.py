from utils import *
import os

mock_data_path = os.path.join(get_dir_abs_path(__file__), "mock_data")


def read_mock_txt(file_name: str):
    return read_csv_as_array(os.path.join(mock_data_path, file_name), has_one_column=True)


pl_male_names = read_mock_txt("PL-male_names.txt")
pl_female_names = read_mock_txt("PL-female_names.txt")
pl_surnames = read_mock_txt("PL-surnames.txt")
