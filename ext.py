import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_uuid():
    return uuid.uuid4().hex


weight_units = [{'name': 'cm', 'value': 0}, {'name': 'ft', 'value': 1}, {'name': 'in', 'value': 2}, {'name': 'm', 'value': 3}]

lwh_units = [{'name': 'g', 'value': 0}, {'name': 'kg', 'value': 1}, {'name': 'lb', 'value': 2}, {'name': 'oz', 'value': 3}]
