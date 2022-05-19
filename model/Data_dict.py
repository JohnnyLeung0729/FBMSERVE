# coding: utf-8
from ext import db, get_uuid


class DataDict(db.Model):
    __tablename__ = 'data_dict'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    pid = db.Column(db.String(32), info='上一级编号')
    code = db.Column(db.String(32), info='编号')
    name = db.Column(db.String(16), info='名称')
    memo = db.Column(db.String(255), info='备注')
    memo1 = db.Column(db.String(255), info='备注1')
    ver = db.Column(db.String(16), info='版本号')
    addtime = db.Column(db.DateTime, info='添加时间')
    edittime = db.Column(db.DateTime, info='修改时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
