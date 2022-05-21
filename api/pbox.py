from flask import Blueprint, request
from flask_restful import Api, Resource

from model.Pbox import Pbox
from util.json import to_json, list_to_json

pbox = Blueprint('pbox', __name__, template_folder='views')

api = Api(pbox)


class ListPbox(Resource):
    def get(self):
        d = Pbox.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListPbox, '/pbox/list')


class PagersPbox(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Pbox.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersPbox, '/pbox/pagers')


class LockPbox(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockPbox, '/pbox/lock')


class DelPbox(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelPbox, '/pbox/del')


class AddPbox(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddPbox, '/pbox/add')


class EditPbox(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditPbox, '/pbox/edit')
