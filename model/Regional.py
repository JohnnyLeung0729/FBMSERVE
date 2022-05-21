# coding: utf-8
from ext import db, get_uuid


class Regional(db.Model):
    __tablename__ = 'regional'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(16), info='地区数据名称')
    code = db.Column(db.String(32), info='简码')
    enname = db.Column(db.String(32), info='地区数据英文名称')
    adder = db.Column(db.String(32), info='添加人')
    addtime = db.Column(db.DateTime, info='添加时间')
    editer = db.Column(db.String(32), info='编辑人')
    edittime = db.Column(db.DateTime, info='编辑时间')
    memo = db.Column(db.String(255), info='备注')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
