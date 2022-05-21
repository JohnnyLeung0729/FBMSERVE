# coding: utf-8
from ext import db, get_uuid


class Language(db.Model):
    __tablename__ = 'language'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    interkey = db.Column(db.String(32), info='国际化key')
    chinese = db.Column(db.String(32), info='中文')
    english = db.Column(db.String(32), info='英文')
    russia = db.Column(db.String(32), info='俄文')
    japanese = db.Column(db.String(32), info='日文')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.interkey

    def __repr__(self):
        return self.id
