from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Data_dict import DataDict
from model.Department import Department
from util.json import to_json, list_to_json

datadict = Blueprint('datadict', __name__, template_folder='views')

api = Api(datadict)


class ListDatadict(Resource):
    def get(self):
        d = DataDict.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListDatadict, '/datadict/list')


class PagersDatadict(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = DataDict.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersDatadict, '/datadict/pagers')


class LockDatadict(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockDatadict, '/datadict/lock')


class DelDatadict(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelDatadict, '/datadict/del')


class AddDatadict(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddDatadict, '/datadict/add')


class EditDatadict(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditDatadict, '/datadict/edit')
