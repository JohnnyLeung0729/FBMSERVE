from flask import Blueprint
from flask_restful import Api, Resource

from ext import  db
from model.Category import Category

category = Blueprint('category', __name__, template_folder='views')

api = Api(category)


# 列出所有分类数据
class ListCategoryAll(Resource):
    def get(self):
        categorys = Category.query.all()
        print(type(categorys))
        return {'code': 200, 'msg': 'ok', 'success': str(categorys)}


api.add_resource(ListCategoryAll, '/category/list')


# 按分页信息列出分类信息
class ListCategoryPage(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'success': 'ListCategoryPage'}


api.add_resource(ListCategoryPage, '/category/listpage')


# 添加分类信息
class AddCategory(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'success': 'AddCategory'}


api.add_resource(AddCategory, '/category/add')


# 编辑分类信息
class EditCategory(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'success': 'EditCategory'}


api.add_resource(EditCategory, '/category/edit')
