from flask import Blueprint, request
from flask_restful import Api, Resource

from model.consumable import Consumable
from util.json import to_json, list_to_json

consumable = Blueprint('consumable', __name__, template_folder='views')

api = Api(consumable)


class ListConsumable(Resource):
    def get(self):
        d = Consumable.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListConsumable, '/consumable/list')


class PagersConsumable(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Consumable.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersConsumable, '/consumable/pagers')


class LockConsumable(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockConsumable, '/consumable/lock')


class DelConsumable(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelConsumable, '/consumable/del')


class AddConsumable(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddConsumable, '/consumable/add')


class EditConsumable(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditConsumable, '/consumable/edit')
