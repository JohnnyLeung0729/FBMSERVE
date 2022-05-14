from flask import Blueprint, request
from flask_restful import Api, Resource

sku = Blueprint('sku', __name__, template_folder='views')

api = Api(sku)


# 测试接口反馈
class GetHelloworld(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'success': 'helloworld'}


api.add_resource(GetHelloworld, '/helloworld')
