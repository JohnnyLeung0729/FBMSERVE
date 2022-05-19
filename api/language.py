from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Department import Department
from model.language import Language
from util.json import to_json, list_to_json

language = Blueprint('language', __name__, template_folder='views')

api = Api(language)


class ListLanguage(Resource):
    def get(self):
        d = Language.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListLanguage', 'data': dd}


api.add_resource(ListLanguage, '/language/list')


class PagersLanguage(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Language.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersLanguage', 'data': dd}


api.add_resource(PagersLanguage, '/language/pagers')


class LockLanguage(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockLanguage, '/language/lock')


class DelLanguage(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelLanguage, '/language/del')


class AddLanguage(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddLanguage, '/language/add')


class EditLanguage(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditLanguage, '/language/edit')
