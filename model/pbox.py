# coding: utf-8
from ext import db, get_uuid


class Pbox(db.Model):
    __tablename__ = 'pbox'

    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(32))
    code = db.Column(db.String(32))
    type = db.Column(db.String(32))
    addtime = db.Column(db.DateTime)
    memo = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
