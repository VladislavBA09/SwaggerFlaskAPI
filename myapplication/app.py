from flasgger import Swagger
from flask import Flask

from .api_routes import admin
from .config import DefaultConfig
from .constanta import NUMBER
from .create_fill_database import (combination_students,
                                   generate_random_groups, main_logic_course)
from .database import (create_database_structure, populate_database_course,
                       populate_database_group)
from .processor import get_engine, get_session


def create_app(config_object) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    Swagger(app)
    app.register_blueprint(admin)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_object.DATA_BASE

    with app.app_context():
        create_database_structure(get_engine())
        with get_session() as session:
            populate_database_group(generate_random_groups(), session)
            populate_database_course(
                main_logic_course(config_object.PATH_FILE),
                session
            )
            combination_students(config_object.PATH_FILE, session, NUMBER)
    return app


def run_app() -> any:
    return create_app(DefaultConfig).run()
