# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Consumable(db.Model):
    __tablename__ = 'consumable'

    id = db.Column(db.String(32), primary_key=True, info='ID')
    name = db.Column(db.String(32), info='耗材名称')
    barcode = db.Column(db.String(64), info='耗材条码')
    material = db.Column(db.String(32), info='材质')
    shape = db.Column(db.String(32), info='形状')
    long = db.Column(db.Numeric(9, 2), info='长')
    width = db.Column(db.Numeric(9, 2), info='宽')
    heigh = db.Column(db.Numeric(9, 2), info='高')
    property = db.Column(db.String(32), info='属性')
    memo = db.Column(db.String(255), info='说明')
    addtime = db.Column(db.DateTime, info='添加时间')
    adder = db.Column(db.String(32), info='添加人')
