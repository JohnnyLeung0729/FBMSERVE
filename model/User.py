# coding: utf-8
from datetime import datetime

from sqlalchemy import DateTime

from ext import db, get_uuid


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    department = db.Column(db.String(32), info='部门')
    post = db.Column(db.Text, info='岗位')
    role = db.Column(db.Text, info='角色')
    account = db.Column(db.String(32), info='账号')
    pwd = db.Column(db.String(32), info='密码')
    email = db.Column(db.String(32), info='邮箱')
    name = db.Column(db.String(32), info='姓名')
    nickname = db.Column(db.String(16), info='昵称')
    phone = db.Column(db.String(32), info='电话')
    sex = db.Column(db.Integer, info='性别')
    active = db.Column(db.Integer, info='状态')
    memo = db.Column(db.String(255), info='备注')
    addtime = db.Column(db.DateTime, info='添加时间')
    type = db.Column(db.String(32), info='用户类型')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
