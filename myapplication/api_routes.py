from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .exception import DataNotFound
from .processor import (additional_course, delete_course, delete_groups,
                        delete_students, delete_students_from_course,
                        get_info_about_course, get_info_about_group, get_list,
                        get_list_with_course, get_list_with_groups,
                        get_student, post_new_course, post_new_groups,
                        post_student, post_student_on_course,
                        put_new_info_course, update_info_for_students,
                        update_info_group)

admin = Blueprint('admin', __name__)
api = Api(admin)

parser = reqparse.RequestParser()
parser.add_argument(
    'data', default=None, required=True, location='form', type=str
)


class ListStudents(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'group_id',
            default=None,
            required=True,
            location='form',
            type=int
        )
        self.parser.add_argument(
            'first_name',
            default=None,
            required=True,
            location='form',
            type=str
        )
        self.parser.add_argument(
            'last_name',
            default=None,
            required=True,
            location='form',
            type=str
        )

    @swag_from('swagger/get/list.yml')
    def get(self) -> list:
        return get_list()

    @swag_from('swagger/post/create_student.yml')
    def post(
            self
    ) -> tuple[dict[str, str], HTTPStatus] | tuple[dict[str, any], HTTPStatus]:
        args = self.parser.parse_args()
        try:
            student_data = post_student(
                args['group_id'],
                args['first_name'],
                args['last_name']
            )
        except ValueError as error:
            return {'error': str(error)}, HTTPStatus.BAD_REQUEST
        return {'group_name': student_data}, HTTPStatus.CREATED


class Student(Resource):

    @swag_from('swagger/get/one_student.yml')
    def get(
            self,
            student_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict:
        try:
            students = get_student(student_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return students

    @swag_from('swagger/put/update_student_info.yml')
    def put(
            self,
            student_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict[str, any]:
        args = parser.parse_args()
        try:
            info = update_info_for_students(student_id, args['data'])
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return {'new_description': info}

    @swag_from('swagger/delete/delete_student.yml')
    def delete(self, student_id: int):
        try:
            delete_students(student_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND


class ListCourse(Resource):
    @swag_from('swagger/get/list_with_course.yml')
    def get(self) -> list:
        return get_list_with_course()

    @swag_from('swagger/post/create_course.yml')
    def post(
            self
    ) -> tuple[dict[str, str], HTTPStatus] | tuple[dict[str, str], HTTPStatus]:
        args = parser.parse_args()
        try:
            course_data = post_new_course(args['data'])
        except ValueError as error:
            return {'error': str(error)}, HTTPStatus.BAD_REQUEST
        return {'course_name': course_data}, HTTPStatus.CREATED


class Course(Resource):

    @swag_from('swagger/get/course.yml')
    def get(
            self,
            course_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict[str, any]:
        try:
            info = get_info_about_course(course_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return info

    @swag_from('swagger/put/course.yml')
    def put(
            self,
            course_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict[str, any]:
        args = parser.parse_args()
        try:
            info = put_new_info_course(course_id, args['data'])
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return {'new_description': info}

    @swag_from('swagger/delete/delete_course.yml')
    def delete(
            self,
            course_id: int
    ) -> tuple[dict[str, str], HTTPStatus]:
        try:
            delete_course(course_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND


class ListGroups(Resource):
    @swag_from('swagger/get/groups.yml')
    def get(self) -> list:
        return get_list_with_groups()

    @swag_from('swagger/post/create_groups.yml')
    def post(
            self
    ) -> tuple[dict[str, str], HTTPStatus] | tuple[dict[str, str], HTTPStatus]:
        args = parser.parse_args()
        try:
            groups_data = post_new_groups(args['data'])
        except ValueError as error:
            return {'error': str(error)}, HTTPStatus.BAD_REQUEST
        return {'group_name': groups_data}, HTTPStatus.CREATED


class Groups(Resource):
    @swag_from('swagger/get/get_group.yml')
    def get(
            self,
            group_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict:
        try:
            info = get_info_about_group(group_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return info

    @swag_from('swagger/put/rename_group.yml')
    def put(
            self,
            group_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | dict[str, any]:
        args = parser.parse_args()
        try:
            info = update_info_group(group_id, args['data'])
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return {'new_description': info}

    @swag_from('swagger/delete/delete_group.yml')
    def delete(
            self,
            group_id: int
    ) -> tuple[dict[str, str], HTTPStatus]:
        try:
            delete_groups(group_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND


class AdditionalChange(Resource):
    @swag_from('swagger/get/list_student_on_course.yml')
    def get(
            self,
            course_id: int
    ) -> tuple[dict[str, str], HTTPStatus] | list:
        try:
            info = additional_course(course_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return info


class DeleteStudentFromCourse(Resource):
    @swag_from('swagger/post/add_student_on_course.yml')
    def post(
            self,
            course_id: int,
            student_id: int
    ) -> (tuple[dict[str, str], HTTPStatus]
          | tuple[dict[str, int], HTTPStatus]):
        try:
            post_student_on_course(student_id, course_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND
        return {
            'student_id': student_id,
            'course_id': course_id
        }, HTTPStatus.CREATED

    @swag_from('swagger/delete/additional.yml')
    def delete(
            self,
            course_id: int,
            student_id: int
    ) -> tuple[dict[str, str], HTTPStatus]:
        try:
            delete_students_from_course(course_id, student_id)
        except DataNotFound as error:
            return {'error': str(error)}, HTTPStatus.NOT_FOUND


api.add_resource(ListStudents, '/students/')
api.add_resource(Student, '/students/<int:student_id>')

api.add_resource(ListCourse, '/course/')
api.add_resource(Course, '/course/<int:course_id>')

api.add_resource(ListGroups, '/groups/')
api.add_resource(Groups, '/groups/<int:group_id>')

api.add_resource(
    AdditionalChange, '/course/<int:course_id>/students'
)

api.add_resource(
    DeleteStudentFromCourse,
    '/courses/<int:course_id>/students/<int:student_id>'
)
