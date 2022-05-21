from flask import Blueprint, request
from flask_restful import Api, Resource

from model.Regional import Regional
from util.json import to_json, list_to_json

regional = Blueprint('regional', __name__, template_folder='views')

api = Api(regional)


class ListRegional(Resource):
    def get(self):
        d = Regional.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListRegional, '/regional/list')


class PagersRegional(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Regional.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersRegional, '/regional/pagers')


class LockRegional(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockRegional, '/regional/lock')


class DelRegional(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelRegional, '/regional/del')


class AddRegional(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddRegional, '/regional/add')


class EditRegional(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditRegional, '/regional/edit')
