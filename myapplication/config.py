from os import environ as env


class TestConfig:
    TESTING = True
    PATH_FILE = 'test_data'
    DATA_BASE = 'sqlite://'


class DefaultConfig:
    DEBUG = True
    PATH_FILE = env.get('PATH_FILE', 'input_data')
    DATA_BASE = env.get('DATA_BASE', 'sqlite:///database.db')
