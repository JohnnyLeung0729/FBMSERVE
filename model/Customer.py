# coding: utf-8
from ext import db, get_uuid


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    username = db.Column(db.String(32), info='用户名')
    cuscode = db.Column(db.String(32), info='客户编号')
    name = db.Column(db.String(32), info='客户名称【全称】')
    abbname = db.Column(db.String(32), info='客户简称\\n')
    active = db.Column(db.Integer, info='状态')
    type = db.Column(db.String(32), info='类型')
    adddtime = db.Column(db.DateTime, info='添加时间')
    paytype = db.Column(db.String(32), info='支付类型')
    pwd = db.Column(db.String(64), info='密码')
    email = db.Column(db.String(128), info='邮箱')
    phone = db.Column(db.String(32), info='电话号码')
    creadit = db.Column(db.Numeric(9, 2), info='授信额度')
    department = db.Column(db.String(32), info='所属部门')
    saler = db.Column(db.String(32), info='所属销售')
    cusservice = db.Column(db.String(32), info='所属客服')
    cussource = db.Column(db.String(32), info='客户来源')
    cuslevel = db.Column(db.String(32), info='客户等级')
    address = db.Column(db.String(255), info='联系地址')
    contact = db.Column(db.String(32), info='联系人')
    contact_phone = db.Column(db.String(32), info='联系人电话')
    idno = db.Column(db.String(128), info='身份证号码')
    idront_url = db.Column(db.String(255), info='身份证正面图像地址')
    idback_url = db.Column(db.String(255), info='身份证背面图像地址')
    authactive = db.Column(db.Integer, info='认证状态')
    authmemo = db.Column(db.String(255), info='认证   允许/拒绝（备注）')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id
