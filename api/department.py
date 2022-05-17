from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Department import Department

department = Blueprint('department', __name__, template_folder='views')

api = Api(department)


# 测试接口反馈
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
