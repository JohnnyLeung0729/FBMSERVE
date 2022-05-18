from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Department import Department
from util.json import to_json, list_to_json

department = Blueprint('department', __name__, template_folder='views')

api = Api(department)


# 添加部门
class AddDepartment(Resource):
    def post(self):
        depinfo = request.get_json()
        print(depinfo)
        department = Department()
        department.pid = depinfo['pid']
        department.name = depinfo['name']
        department.email = depinfo['email']
        department.phone = depinfo['phone']
        department.type = depinfo['deptype']
        department.code = depinfo['depcode']
        department.responsibler = depinfo['responser']
        department.sort = depinfo['dispindex']
        department.active = depinfo['active']
        department.memo = depinfo['memo']
        db.session.add(department)
        db.session.commit()
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddDepartment, '/department/add')


class ListDepartment(Resource):
    def get(self):
        dl = Department.query.order_by(Department.sort.asc()).all()
        dlt = list_to_json(dl)
        return {'code': 200, 'msg': 'TRUE', 'data': dlt}


api.add_resource(ListDepartment, '/department/list')


class DelDepartment(Resource):
    def post(self):
        depinfo = request.get_json()
        did = depinfo['id']
        dep = Department.query.filter(Department.id == did).first()
        db.session.delete(dep)
        db.session.commit()
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelDepartment, '/department/del')


class EditDepartment(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditDepartment, '/department/edit')
