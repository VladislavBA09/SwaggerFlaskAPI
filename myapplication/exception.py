from .database import Course, Group, Student


class DataNotFound(Exception):
    pass


def find_student_by_id(student_id: int, session: any) -> Student:
    student = session.query(
        Student).where(Student.id == student_id).one_or_none()
    if not student:
        raise DataNotFound(f'Student with ID {student_id} not found.')
    return student


def find_course_by_id(course_id: int, session: any) -> Course:
    course = session.query(
        Course).where(Course.id == course_id).one_or_none()
    if not course:
        raise DataNotFound(f'Course with ID {course_id} not found.')
    return course


def find_group_by_id(group_id: int, session: any) -> Course:
    course = session.query(
        Group).where(Group.id == group_id).one_or_none()
    if not course:
        raise DataNotFound(f'Group with ID {group_id} not found.')
    return course
