import random

from .database import Course, Group, Student, association_table


def get_course_from_database(session) -> list[dict]:
    new_list = []
    data = session.query(Course)
    for element in data:
        new_list.append(element.name
                        )
    return new_list


def change_course_students(
        new_list: list,
        number_student: int,
        session
) -> dict:
    for elements in new_list:
        for key, values in elements.items():
            if number_student in values:
                change_type_value = ''.join(
                    random.sample(
                        get_course_from_database(session),
                        k=1))

                dict_data = {
                    'additional_course': change_type_value
                }
                return {**elements, **dict_data}


def processor(
        new_id: str,
        process,
        session
) -> list:
    new = []
    for element in new_id:
        for char in random.sample(process(session), k=3):
            new.append({element: char})
    return new


def check_association_table(
        session,
        number: int
) -> list:
    new_list = []
    list_course = session.query(
        association_table).where(
        association_table.columns.student_id == number)
    for element in list_course:
        new_list.append(element.course_id)
    return new_list


def get_groups_from_database(session) -> list:
    new_list = []
    data = (session
            .query(Group))
    for element in data:
        new_list.append(element.group)
    return new_list


def get_groups_students(list_students: list) -> list:
    new_list = []
    for element in range(0, len(list_students), 30):
        new_list.append(list_students[element:element + 30])

    return new_list


def get_id_course_from_database(session) -> list[dict]:
    new_list = []
    data = session.query(Course)
    for element in data:
        new_list.append(element.id
                        )
    return new_list


def get_id_students_from_database(session) -> list:
    new_list = []
    data = session.query(Student)
    for element in data:
        new_list.append(element.id)
    return new_list


def get_association_data(
        session,
        students_id_list: list
) -> list:
    new_list = []
    for element in students_id_list:
        data_course = session.query(Course).where(Course.id == element)
        for data in data_course:
            new_list.append(data.name)
    return new_list


def get_data_from_association(session) -> list:
    new_list = []
    data = session.query(association_table)
    for element in data:
        new_list.append({element.student_id: element.course_id})
    return new_list


def get_course_id(session) -> list:
    input_list = get_data_from_association(session)
    new_list = []
    for element in input_list:
        for key, value in element.items():
            data = session.query(Course).where(Course.id == value)
            for data in data:
                new_list.append({'key': key, 'value': data.name})
    return new_list


def check_duplicate_key(list_of_dicts: list) -> dict:
    result_dict = {}
    for data in list_of_dicts:
        key = data["key"]
        value = data["value"]

        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    return result_dict


def get_additional_course_info(
        session,
        new_id: int
) -> list:
    list_course_id = []
    output_data_course = session.query(
        association_table
    ).where(association_table.columns.course_id == new_id)
    for element in output_data_course:
        list_course_id.append(element.student_id)
    return list_course_id
