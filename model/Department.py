# coding: utf-8
from ext import db, get_uuid


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    pid = db.Column(db.String(32), info='上级部门')
    type = db.Column(db.String(32), info='部门类型')
    code = db.Column(db.String(32), info='部门编码')
    name = db.Column(db.String(16), info='部门名称')
    responsibler = db.Column(db.String(45), info='部门负责人')
    email = db.Column(db.String(45), info='邮箱')
    phone = db.Column(db.String(32), info='电话')
    sort = db.Column(db.Integer, info='显示顺序')
    active = db.Column(db.Integer, info='状态')
    memo = db.Column(db.String(255), info='备注')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
