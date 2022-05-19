# coding: utf-8
from ext import db, get_uuid


class Cuslevel(db.Model):
    __tablename__ = 'cuslevel'

    id = db.Column(db.String(32), primary_key=True, info='ID')
    name = db.Column(db.String(16), info='客户等级名称')
    addtime = db.Column(db.DateTime, info='添加时间')
    memo = db.Column(db.String(255), info='备注')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id

