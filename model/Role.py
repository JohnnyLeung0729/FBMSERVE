# coding: utf-8
from ext import db, get_uuid


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(16), info='角色名称')
    tag = db.Column(db.String(32))
    power = db.Column(db.String, info='权限')
    sort = db.Column(db.Integer, info='显示顺序')
    active = db.Column(db.Integer, info='状态')
    memo = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
