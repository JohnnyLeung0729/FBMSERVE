# coding: utf-8
from ext import db, get_uuid


class Sku(db.Model):
    __tablename__ = 'sku'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid(), info='ID')
    name = db.Column(db.String(32), info='SKU商品名称')
    abbname = db.Column(db.String(32), info='SKU简称')
    enname = db.Column(db.String(64), info='英文品牌名')
    cargo_no = db.Column(db.String(32), info='货号')
    upc = db.Column(db.String(32), info='产品代码UPC')
    model_cp = db.Column(db.String(32), info='产品型号')
    cus_id = db.Column(db.String(32), info='所属客户')
    class_id = db.Column(db.String(32), info='类别名称')
    unit = db.Column(db.String(32), info='单位')
    bigtype = db.Column(db.Integer, info='是否为大货')
    color = db.Column(db.String(32), info='颜色')
    size = db.Column(db.Numeric(11, 2), info='尺寸')
    weight = db.Column(db.Numeric(11, 2), info='重量')
    price = db.Column(db.Numeric(11, 2), info='单价')
    parkaging = db.Column(db.String(32), info='包装材料')
    length = db.Column(db.Numeric(9, 2), info='长')
    width = db.Column(db.Numeric(9, 2), info='宽')
    height = db.Column(db.Numeric(9, 2), info='高')
    shelf_life = db.Column(db.Numeric(6, 2), info='保质期（天）')
    safe_quantity = db.Column(db.String(32), info='安全库存')
    inventory_uper = db.Column(db.Numeric(11, 2), info='库存上限')
    inventory_lower = db.Column(db.Numeric(11, 2), info='库存下限')
    specifi = db.Column(db.String(32), info='规格')
    inspection_type = db.Column(db.String(32), info='检验类型')
    inmater_price = db.Column(db.Numeric(11, 2), info='来料上架单价')
    cusdec_chinese = db.Column(db.String(32), info='中文报关名')
    cusdec_eng = db.Column(db.String(64), info='英文报关名')
    cusdec_code = db.Column(db.String(32), info='报关编码')
    spu = db.Column(db.String(32), info='SPU')
    cusdec_price = db.Column(db.Numeric(11, 2), info='报关价格（USD）')
    pic_url = db.Column(db.String(256), info='图片地址')
    combined = db.Column(db.Integer, info='是否组合产品')
    conversion_auto = db.Column(db.Integer, info='自动库存转换')
    addtime = db.Column(db.DateTime, info='添加时间')
    adder = db.Column(db.String(32), info='添加人')
    memo = db.Column(db.String(128), info='备注')
    active = db.Column(db.Integer, info='状态_')
    typ = db.Column(db.String(32), info='类型_')
    weight_unit = db.Column(db.String(8), info='重量单位')
    lwh_unit = db.Column(db.String(8), info='长宽高单位')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id