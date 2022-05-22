import json

from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db, get_datetime_now
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


class AddUser(Resource):
    def post(self):
        c = request.get_json()
        department = c['department']
        post = c['post']
        role = c['role']
        account = c['account']
        pwd = c['pwd']
        email = c['email']
        name = c['name']
        abbname = c['abbname']
        phone = c['phone']
        sex = c['sex']
        active = c['active']
        memo = c['memo']
        type = c['type']

        cc = User()
        cc.addtime = get_datetime_now()
        cc.post = post
        cc.department = department
        cc.role = role
        cc.account = account
        cc.pwd = pwd
        cc.email = email
        cc.name = name
        cc.nickname = abbname
        cc.phone = phone
        cc.sex = sex
        cc.active = active
        cc.memo = memo
        cc.type = type

        db.session.add(cc)
        db.session.commit()

        return {'code': 200, 'msg': 'ok', 'success': 'AddUser'}


api.add_resource(AddUser, '/user/add')


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
        u = User.query.filter(User.account == logininfo['username'],
                              User.pwd == password_md5(logininfo['password'])).first()
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
