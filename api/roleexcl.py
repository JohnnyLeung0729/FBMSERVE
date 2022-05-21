from flask import Blueprint, request
from flask_restful import Api, Resource

from model.Role_excl import RoleExcl
from util.json import to_json, list_to_json

roleexcl = Blueprint('roleexcl', __name__, template_folder='views')

api = Api(roleexcl)


class ListRoleexcl(Resource):
    def get(self):
        d = RoleExcl.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListRoleexcl, '/roleexcl/list')


class PagersRoleexcl(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = RoleExcl.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersRoleexcl, '/roleexcl/pagers')


class LockRoleexcl(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockRoleexcl, '/roleexcl/lock')


class DelRoleexcl(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelRoleexcl, '/roleexcl/del')


class AddRoleexcl(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddRoleexcl, '/roleexcl/add')


class EditRoleexcl(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditRoleexcl, '/datadict/edit')
