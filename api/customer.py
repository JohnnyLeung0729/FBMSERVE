from flask import Blueprint, request
from flask_restful import Api, Resource

from model.Customer import Customer
from util.json import to_json, list_to_json

customer = Blueprint('customer', __name__, template_folder='views')

api = Api(customer)


class ListCustomer(Resource):
    def get(self):
        d = Customer.query.all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'ListDatadict', 'data': dd}


api.add_resource(ListCustomer, '/customer/list')


class PagersCustomer(Resource):
    def get(self):
        ps = int(request.args.get('page_size'))
        po = int(request.args.get('page_one'))
        ofs = ps * (po - 1)
        d = Customer.query.offset(ofs).limit(ps).all()
        dd = list_to_json(d)
        return {'code': 200, 'msg': 'ok', 'success': 'PagersDatadict', 'data': dd}


api.add_resource(PagersCustomer, '/customer/pagers')


class LockCustomer(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(LockCustomer, '/customer/lock')


class DelCustomer(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelCustomer, '/customer/del')


class AddCustomer(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(AddCustomer, '/customer/add')


class EditCustomer(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditCustomer, '/customer/edit')
