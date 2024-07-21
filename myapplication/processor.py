from flask import current_app, g
from sqlalchemy import create_engine, delete, insert, update
from sqlalchemy.orm import sessionmaker

from .additional import (check_duplicate_key, get_additional_course_info,
                         get_course_id, get_id_course_from_database,
                         get_id_students_from_database, processor)
from .database import (Course, Group, Student, association_table,
                       populate_database_association_table)
from .exception import (DataNotFound, find_course_by_id, find_group_by_id,
                        find_student_by_id)


def get_engine():
    if not hasattr(current_app, '_db'):
        current_app._db = create_engine(
            current_app.config['DATA_BASE'], echo=True
        )
    return current_app._db


def get_session():
    if not hasattr(g, '_session'):
        g._session = sessionmaker(bind=get_engine())
    return g._session()


def get_list() -> list:
    new_list = []
    with get_session() as session:
        data = session.query(Student)
        for element in data:
            new_list.append({'group_id': f'{element.group_id}',
                             'first_name': element.first_name,
                             'last_name': element.last_name}
                            )
    return new_list


def post_student(
        group_id: int,
        first_name: str,
        last_name: str,
):
    if len(first_name) == 0 or len(last_name) == 0:
        raise DataNotFound(
            'Parameters first_name, last_name  must be non-empty'
        )
    with get_session() as session:
        group = session.query(
            Group
        ).where(Group.id == group_id).one_or_none()
        if group_id and not group:
            raise DataNotFound(
                f'Group with ID {group_id} does not exist'
            )

        input_data = insert(Student).values(
            group_id=group.name,
            first_name=first_name,
            last_name=last_name,
            description='None'
        )
        session.execute(input_data)
        session.commit()
        return group.name


def get_student(
        student_id: int,
) -> dict:
    with get_session() as session:
        student = find_student_by_id(student_id, session)
        data = {
            'group_id': f'{student.group_id}',
            'first_name': student.first_name,
            'last_name': student.last_name}
        return data


def update_info_for_students(
        student_id: int,
        put_data: str
) -> str:
    with get_session() as session:
        find_student_by_id(student_id, session)
        output_data = update(Student).where(
            Student.id == student_id
        ).values(description=put_data)
        session.execute(output_data)
        session.commit()
        return put_data


def delete_students(
        student_id: int,
) -> any:
    with get_session() as session:
        find_student_by_id(student_id, session)
        stmt = delete(Student).where(Student.id == student_id)
        session.execute(stmt)
        session.commit()


def func_fill() -> any:
    with get_session() as session:
        data_students = get_id_students_from_database(session)
        return populate_database_association_table(
            session,
            data_students,
            get_id_course_from_database,
            processor
        )


def get_list_with_course() -> list:
    func_fill()
    with get_session() as session:
        data_student = get_list()
        data_course = get_course_id(session)
        output_dict = check_duplicate_key(data_course)
        for element in data_student:
            for key, value in output_dict.items():
                element['course'] = value
        return data_student


def post_new_course(
        data: str
) -> str:
    with get_session() as session:
        insert_data = insert(Course).values(
            name=data,
            description='None'
            )
        session.execute(insert_data)
        session.commit()
        return data


def get_info_about_course(
        course_id: int
) -> dict[str, any]:
    with get_session() as session:
        find_course_by_id(course_id, session)
        output_data = session.query(Course).where(Course.id == course_id)
        for element in output_data:
            data = {
                'id': element.id,
                'name': element.name,
                'description': element.description}
            return data


def put_new_info_course(
        course_id: int,
        put_data: str
) -> any:
    with get_session() as session:
        find_course_by_id(course_id, session)
        output_data = update(Course).where(
            Course.id == course_id
        ).values(description=put_data)
        session.execute(output_data)
        session.commit()
        return put_data


def delete_course(
        course_id: int,
):
    with get_session() as session:
        find_course_by_id(course_id, session)
        stmt = delete(Course).where(Course.id == course_id)
        session.execute(stmt)
        session.commit()


def get_list_with_groups() -> list:
    with get_session() as session:
        new_list = []
        input_data = session.query(Group)
        for element in input_data:
            new_list.append({'name': element.name,
                             'description': element.description})
        return new_list


def post_new_groups(
        data: str
) -> str:
    with get_session() as session:
        insert_data = insert(Group).values(
            name=data,
            description='None'
        )
        session.execute(insert_data)
        session.commit()
        return data


def get_info_about_group(
        group_id: int
) -> dict:
    with get_session() as session:
        find_group_by_id(group_id, session)
        data = session.query(Group).where(Group.id == group_id)
        for element in data:
            new_dict = {'id': element.id,
                        'name': element.name,
                        'description': element.description}
        return new_dict


def update_info_group(
        group_id: int,
        info: str
):
    with get_session() as session:
        find_group_by_id(group_id, session)
        output_data = update(Group).where(
            Group.id == group_id
        ).values(description=info)
        session.execute(output_data)
        session.commit()
        return info


def delete_groups(
        group_id: int,
):
    with get_session() as session:
        find_group_by_id(group_id, session)
        stmt = delete(Group).where(Group.id == group_id)
        session.execute(stmt)
        session.commit()


def additional_course(
        course_id: int
) -> list:
    with get_session() as session:
        find_course_by_id(course_id, session)
        new_list = []
        input_data = get_additional_course_info(session, course_id)
        for element in input_data:
            output_data = session.query(
                Student
            ).where(Student.id == str(element))
            for data in output_data:
                new_list.append(
                    {'group_id': data.group_id,
                     'first_name': data.first_name,
                     'last_name': data.last_name}
                )
        return new_list


def post_student_on_course(
        student_id: int,
        course_id: int
) -> any:
    with get_session() as session:
        find_course_by_id(course_id, session)
        find_student_by_id(student_id, session)
        input_data = insert(association_table).values(
            student_id=student_id,
            course_id=course_id
        )
        session.execute(input_data)
        session.commit()


def delete_students_from_course(
        course_id: int,
        student_id: int,
):
    with get_session() as session:
        find_course_by_id(course_id, session)
        find_student_by_id(student_id, session)
        input_data = delete(association_table).where(
            association_table.columns.student_id == student_id
        ).where(association_table.columns.course_id == course_id)
        session.execute(input_data)
        session.commit()
