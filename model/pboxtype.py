# coding: utf-8
from ext import db, get_uuid


class Pboxtype(db.Model):
    __tablename__ = 'pboxtype'

    id = db.Column(db.String(32), primary_key=True, info='ID')
    code = db.Column(db.String(32), info='拣货箱类型编码')
    name = db.Column(db.String(32), info='拣货箱类型名称')
    active = db.Column(db.Integer, info='拣货箱状态')
    long = db.Column(db.Numeric(9, 2), info='拣货箱长')
    width = db.Column(db.Numeric(9, 2), info='拣货箱宽')
    high = db.Column(db.Numeric(9, 2), info='拣货箱高')
    sums = db.Column(db.Numeric(9, 2), info='拣货箱数量')
    memo = db.Column(db.String(255), info='备注')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id

