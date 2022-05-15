from flask import Blueprint
from flask_restful import Api, Resource

user = Blueprint('user', __name__, template_folder='views')

api = Api(user)


# 测试接口反馈
class Postinit(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'UserPostinit'}


api.add_resource(Postinit, '/user')


# 测试接口反馈
class PostLogin(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'UserPostLogin'}


api.add_resource(PostLogin, '/user/login')
