# coding: utf-8
from ext import db, get_uuid


class Warehouse(db.Model):
    __tablename__ = 'warehouse'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(32), info='仓库名称')
    type = db.Column(db.String(32), info='仓库类型')
    op_type = db.Column(db.String(32), info='运营类型')
    responsible = db.Column(db.String(32), info='仓库负责人')
    contact = db.Column(db.String(32), info='联系方式')
    uper = db.Column(db.String(32), info='上级仓库')
    country = db.Column(db.String(32), info='国家')
    province = db.Column(db.String(32), info='省份')
    city = db.Column(db.String(32), info='城市')
    county = db.Column(db.String(32), info='县城')
    postcode = db.Column(db.String(16), info='邮编')
    address = db.Column(db.String(64), info='详细地址')
    adder = db.Column(db.String(32), info='添加人')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
