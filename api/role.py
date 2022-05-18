from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Department import Department
from model.Post import Post
from model.Role import Role
from util.json import to_json, list_to_json

role = Blueprint('role', __name__, template_folder='views')

api = Api(role)


class AddRole(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddRole, '/role/add')


class ListRole(Resource):
    def get(self):
        r = Role.query.order_by(Role.sort.asc()).all()
        dr = list_to_json(r)
        return {'code': 200, 'msg': 'TRUE', 'data': dr}


api.add_resource(ListRole, '/role/list')


class DelRole(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelRole, '/role/del')


class EditRole(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditRole, '/role/edit')