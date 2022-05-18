from flask import Blueprint, request
from flask_restful import Api, Resource

from ext import db
from model.Department import Department
from model.Post import Post
from util.json import to_json, list_to_json

post = Blueprint('post', __name__, template_folder='views')

api = Api(post)


class AddPost(Resource):
    def post(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddDepartment'}


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
