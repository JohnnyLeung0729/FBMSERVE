from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db, get_datetime_now
from model.Department import Department
from model.Post import Post
from util.json import to_json, list_to_json

post = Blueprint('post', __name__, template_folder='views')

api = Api(post)


# Coder: JohnnyLeung
# 20220523
# 添加岗位，接口
class AddPost(Resource):
    def post(self):
        p = request.get_json()
        name = p['name']
        code = p['code']
        sort = p['sort']
        active = p['active']
        memo = p['memo']
        pp = Post()
        pp.name = name
        pp.code = code
        pp.sort = sort
        pp.active = active
        pp.memo = memo
        pp.addtime = get_datetime_now()

        db.session.add(pp)
        db.session.commit()
        return {'code': 200, 'msg': 'ok', 'success': 'AddPost'}


api.add_resource(AddPost, '/post/add')


class ListPost(Resource):
    def get(self):
        p = Post.query.order_by(Post.sort.asc()).all()
        dp = list_to_json(p)
        return {'code': 200, 'msg': 'TRUE', 'data': dp}


api.add_resource(ListPost, '/post/list')


class DelPost(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(DelPost, '/post/del')


class EditPost(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


api.add_resource(EditPost, '/post/edit')
