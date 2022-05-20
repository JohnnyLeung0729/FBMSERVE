from flask import Blueprint, request
from flask_restful import Api, Resource

from model.cuslevel import Cuslevel
from util.json import to_json, list_to_json

cuslevel = Blueprint('cuslevel', __name__, template_folder='views')

api = Api(cuslevel)


class ListCuslevel(Resource):
    def get(self):
        d = Cuslevel.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListCuslevel, '/cuslevel/list')


class PagersCuslevel(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Cuslevel.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersCuslevel, '/cuslevel/pagers')


class LockCuslevel(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockCuslevel, '/cuslevel/lock')


class DelCuslevel(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelCuslevel, '/cuslevel/del')


class AddCuslevel(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddCuslevel, '/cuslevel/add')


class EditCuslevel(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditCuslevel, '/cuslevel/edit')
