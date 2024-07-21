import random

from .models import Course, Group, Student, association_table


def create_database_structure(db):
    Student.metadata.create_all(bind=db)
    Course.metadata.create_all(bind=db)
    Group.metadata.create_all(bind=db)


def populate_database_group(
        data,
        session
):
    session.query(Group).delete()
    for element in data:
        for key, value in element.items():
            data = Group(
                name=key,
                description=value
            )
            session.add(data)
            session.commit()


def populate_database_course(
        data,
        session
):
    session.query(Course).delete()
    for element in data:
        for key, value in element.items():
            student_info = Course(
                name=value['first_name'],
                description=value['description']
            )
            session.add(student_info)
            session.commit()


def populate_database_student(
        group_id,
        data,
        description: str,
        session
):
    session.query(Student).delete()
    for element in data:
        for key, value in element.items():
            student_info = Student(
                group_id=random.choice(group_id),
                first_name=value['first_name'],
                last_name=value['last_name'],
                description=description
            )
            session.add(student_info)
            session.commit()


def populate_database_association_table(
        session,
        data_students: list,
        func,
        processor
):
    session.query(association_table).delete()
    input_data = processor(
        data_students,
        func,
        session
    )
    for element in input_data:
        for key, value in element.items():
            stmt = (
                association_table.insert().values(
                    student_id=key,
                    course_id=value
                ))
            session.execute(stmt)
            session.commit()
