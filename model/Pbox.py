# coding: utf-8
from ext import db, get_uuid


class Pbox(db.Model):
    __tablename__ = 'pbox'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(32), info='拣货箱名称')
    code = db.Column(db.String(32), info='拣货箱编码')
    type = db.Column(db.String(32), info='拣货箱类别{ID}')
    addtime = db.Column(db.DateTime, info='添加时间')
    memo = db.Column(db.String(255), info='备注')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
