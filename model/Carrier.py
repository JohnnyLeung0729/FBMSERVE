# coding: utf-8
from ext import db, get_uuid


class Carrier(db.Model):
    __tablename__ = 'carrier'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    code = db.Column(db.String(16), info='承运商简码')
    name = db.Column(db.String(16), info='承运商名称')
    abbname = db.Column(db.String(16), info='简称')
    enname = db.Column(db.String(32), info='英文名称')
    address = db.Column(db.String(128), info='承运商地址')
    contenter = db.Column(db.String(32), info='联系人')
    phone = db.Column(db.String(16), info='联系电话')
    email = db.Column(db.String(32), info='邮箱')
    country = db.Column(db.String(32), info='国家')
    type = db.Column(db.String(32), info='运输方式')
    webadd = db.Column(db.String(128), info='承运商网址')
    tsocket = db.Column(db.String(256), info='官网物流跟踪地址')
    iscarrier = db.Column(db.Integer, info='是否启用承运商')
    isagent = db.Column(db.Integer, info='是否代理商')
    fine = db.Column(db.Numeric(9, 2), info='惩罚比例')
    servetype = db.Column(db.String(255), info='服务方式')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
