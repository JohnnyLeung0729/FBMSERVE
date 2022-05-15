import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_uuid():
    return uuid.uuid4().hex


weight_units = [{'name': 'cm', 'value': 0}, {'name': 'ft', 'value': 1}, {'name': 'in', 'value': 2},
                {'name': 'm', 'value': 3}]

lwh_units = [{'name': 'g', 'value': 0}, {'name': 'kg', 'value': 1}, {'name': 'lb', 'value': 2},
             {'name': 'oz', 'value': 3}]

department_type = [{'name': '公司', 'value': 0}, {'name': '网点', 'value': 1}, {'name': '部门', 'value': 2}]

user_type = [{'name': '其他员工', 'value': 0}, {'name': '仓库员工', 'value': 1}]
