from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Group(db.Model):
    __table_name__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)
    students = db.relationship('Student', backref='group')


association_table = db.Table(
    'association_table',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


class Student(db.Model):
    __table_name__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    description = db.Column(db.String)
    courses = db.relationship(
        'Course',
        secondary=association_table,
        back_populates='students'
    )


class Course(db.Model):
    __table_name__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    students = db.relationship(
        'Student',
        secondary=association_table,
        back_populates='courses'
    )
