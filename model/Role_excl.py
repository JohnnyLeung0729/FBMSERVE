# coding: utf-8
from ext import db, get_uuid


class RoleExcl(db.Model):
    __tablename__ = 'role_excl'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(16), info='互斥组名名')
    sort = db.Column(db.Integer, info='排序')
    active = db.Column(db.Integer, info='状态')
    excl_role = db.Column(db.String(32), info='互斥角色')
    memo = db.Column(db.String(255), info='备注')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
