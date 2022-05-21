# coding: utf-8
from ext import db, get_uuid


class Warea(db.Model):
    __tablename__ = 'warea'

    id = db.Column(db.String(32), primary_key=True, info='ID')
    name = db.Column(db.String(16), info='库区名称')
    code = db.Column(db.String(32), info='库区编码')
    warehouse_id = db.Column(db.String(32), info='仓库名称【ID】')
    abcclass = db.Column(db.String(16), info='ABC分类')
    floor = db.Column(db.String(8), info='楼层')
    wtype = db.Column(db.String(32), info='库区类型')
    bandtype = db.Column(db.String(32), info='绑定类型')
    memo = db.Column(db.String(255), info='说明备注')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.name
