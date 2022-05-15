# coding: utf-8
from ext import db, get_uuid


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID\\n')
    name = db.Column(db.String(32), info='岗位名称')
    code = db.Column(db.String(32), info='岗位编码')
    sort = db.Column(db.Integer, info='显示顺序')
    active = db.Column(db.Integer, info='状态')
    memo = db.Column(db.String(255), info='备注')
    addtime = db.Column(db.DateTime, info='添加时间\\n')

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.name
