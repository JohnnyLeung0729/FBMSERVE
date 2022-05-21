# coding: utf-8
from ext import db, get_uuid


class Wcol(db.Model):
    __tablename__ = 'wcol'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    warehouseid = db.Column(db.String(32), info='仓库名称')
    wareaid = db.Column(db.String(32), info='库区')
    wareacode = db.Column(db.String(32), info='库区编号')
    wareatype = db.Column(db.String(32), info='库区类型')
    wcolactive = db.Column(db.Integer, info='货列状态')
    memo = db.Column(db.String(255), info='备注说明')
    wcolcodea = db.Column(db.Integer, info='货列编号A')
    wcolcodeb = db.Column(db.Integer, info='货列编号B')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.wareaid

    def __repr__(self):
        return self.id
