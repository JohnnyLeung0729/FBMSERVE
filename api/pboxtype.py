from flask import Blueprint, request
from flask_restful import Api, Resource

from model.Pboxtype import Pboxtype
from util.json import to_json, list_to_json

pboxtype = Blueprint('pboxtype', __name__, template_folder='views')

api = Api(pboxtype)


class ListPboxtype(Resource):
    def get(self):
        d = Pboxtype.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListPboxtype, '/pboxtype/list')


class PagersPboxtype(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Pboxtype.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersPboxtype, '/pboxtype/pagers')


class LockPboxtype(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockPboxtype, '/pboxtype/lock')


class DelPboxtype(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelPboxtype, '/pboxtype/del')


class AddPboxtype(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddPboxtype, '/pboxtype/add')


class EditPboxtype(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditPboxtype, '/pbox/edit')
