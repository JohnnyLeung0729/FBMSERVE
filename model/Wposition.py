# coding: utf-8
from ext import db, get_uuid


class Wposition(db.Model):
    __tablename__ = 'wposition'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    warehouseid = db.Column(db.String(32), info='仓库名称')
    wareaid = db.Column(db.String(32), info='库区ID')
    wareacode = db.Column(db.String(32), info='库区编号')
    wareatype = db.Column(db.String(32), info='库区类型')
    wcolcode = db.Column(db.String(32), info='库列编号')
    shelfcodea = db.Column(db.Integer, info='货架编号A')
    shelfcodeb = db.Column(db.Integer, info='货架编号B')
    shelffloora = db.Column(db.Integer, info='货架层号A \\n')
    shelffloorb = db.Column(db.Integer, info='货架层号B')
    shelfpositiona = db.Column(db.Integer, info='货架格号A ')
    shelfpositionb = db.Column(db.Integer, info='货架格号B')
    wpos_spec = db.Column(db.String(32), info='货位规格')
    wpos_type = db.Column(db.String(32), info='货位类型')
    lwh = db.Column(db.String(32), info='长宽高')
    capacityuper = db.Column(db.String(32), info='容量上限')
    work_sequence = db.Column(db.String(32), info='作业顺序')
    addtime = db.Column(db.DateTime, info='添加时间')

    def __str__(self):
        return self.wareaid

    def __repr__(self):
        return self.id
