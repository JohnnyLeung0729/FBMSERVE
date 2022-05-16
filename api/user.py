import json

from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Sku import Sku
from model.User import User
from util.json import ComplexEncoder, to_json
from util.pwd import password_md5
from util.token import generate_token, certify_token

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
        # tok = generate_token('lineboy23')
        # untok = certify_token('lineboy23', tok)
        # print(tok)
        # print(untok)
        # pwd = password_md5('Ly818379')
        # print(pwd)
        logininfo = request.get_json()
        print(logininfo['username'])
        u = User.query.filter(User.account == logininfo['username'], User.pwd == password_md5(logininfo['password'])).first()
        # u = Sku.query().all()
        print(u)
        if not u:
            return {'code': 000, 'msg': 'FALSE', 'data': None}
        else:
            tok = generate_token(u.account)
            # pp = json.dumps(u, cls=ComplexEncoder)
            # print(pp)
            cc = to_json(u)
            print(cc)
            return {'code': 200, 'msg': 'TRUE', 'data': cc, 'token': tok}


api.add_resource(PostLogin, '/user/login')
