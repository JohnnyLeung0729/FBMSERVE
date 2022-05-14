# coding: utf-8
from ext import db, get_uuid


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(32), info='类别名称')
    check_type = db.Column(db.String(32), info='检查类型')
    samp_pro = db.Column(db.Numeric(10, 0), info='抽检比例')
    warra_per = db.Column(db.Integer, info='保质天数')
    check_point = db.Column(db.String(32), info='检验项')
    memo = db.Column(db.String(255), info='类别描述')
    checker = db.Column(db.String(32), info='质检员')
    pid = db.Column(db.String(32), info='上级类别')
    addtime = db.Column(db.DateTime, info='创建时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
