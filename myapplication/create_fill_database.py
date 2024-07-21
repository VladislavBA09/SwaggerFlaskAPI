import os
import pathlib
import random
import string
from pathlib import Path

from .constanta import COURSES, STUDENTS
from .database import Group, populate_database_student
from .exception import DataNotFound


def search_files(folder: str, constanta: str) -> pathlib.Path:
    if not isinstance(folder, str) and not os.path.isfile(folder):
        raise DataNotFound('The data type error')
    students = next(Path(folder).rglob(constanta))
    return students


def open_data_file_raisers(file: any) -> any:
    with open(file, 'r') as data_file:
        return data_file.readlines()


def get_information(data: any, constanta: str) -> list[str]:
    folder_data = search_files(data, constanta)
    list_students = open_data_file_raisers(folder_data)
    split_data = ''.join(
        list_students
    ).replace('\n', '').split(',')
    return split_data


def generate_random_students(
        data: any,
        number: int
) -> tuple:
    name = random.choices(
        get_information(data, STUDENTS)[0:20], k=number
    )
    sur_name = random.choices(
        get_information(data, STUDENTS)[20::], k=number
    )
    return name, sur_name


def generator_info() -> str:
    return 'None'


def generate_random_string() -> str:
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for _ in range(2))
    rand_numb = random.randint(11, 21)
    return f'{rand_string}-{rand_numb}'


def generate_students(first_name: str, last_name: str) -> list:
    new_list = []
    for elements in range(1, len(first_name)):
        new_list.append(
            {
                elements:
                    {'first_name': first_name[elements],
                     'last_name': last_name[elements],
                     }
             }
        )
    return new_list


def generate_course(first_name: list, description: list) -> list:
    new_list = []
    for elements in range(len(first_name)):
        new_list.append(
            {
                elements:
                    {'first_name': first_name[elements],
                     'description': description[elements],
                     }
             }
        )
    return new_list


def generate_random_groups() -> list[dict[str, any]]:
    new_list = []
    for elements in range(10):
        new_list.append(
            {generate_random_string(): generator_info()})
    return new_list


def main_logic_course(data: any) -> list[str]:
    name = get_information(data, COURSES)[0:10]
    description = get_information(data, COURSES)[10::]
    return generate_course(name, description)


def combination_students(
        data: any,
        session: any,
        number: int
) -> any:
    input_group_list = []
    groups_id = session.query(Group)
    for elements in groups_id:
        input_group_list.append(elements.name)
    input_data_students = (
        generate_students(
            generate_random_students(data, number)[0],
            generate_random_students(data, number)[1])
    )
    output_data = populate_database_student(
        input_group_list, input_data_students,
        generator_info(), session
    )
    return output_data
