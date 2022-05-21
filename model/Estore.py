# coding: utf-8
from ext import db, get_uuid


class Estore(db.Model):
    __tablename__ = 'estore'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    platform = db.Column(db.String(32), info='电商店铺——电商平台')
    customer = db.Column(db.String(32), info='客户名称')
    name = db.Column(db.String(32), info='店铺名称')
    cert = db.Column(db.String(128), info='通行凭证')
    key = db.Column(db.String(128), info='密钥')
    selsid = db.Column(db.String(32), info='卖家ID')
    active = db.Column(db.Integer, info='状态')
    addid = db.Column(db.String(32), info='地点ID')
    memo = db.Column(db.String(255), info='备注')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
