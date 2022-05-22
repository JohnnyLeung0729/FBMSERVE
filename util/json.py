import decimal
from datetime import datetime, date

from flask import json
from sqlalchemy import JSON


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # 处理返回数据中有decimal类型的数据
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def to_json(self):
    dic = {}
    for c in self.__table__.columns:
        if str(c.type) == 'DATETIME':
            dic[c.name] = str(getattr(self, c.name))  # .strftime('%Y-%m-%d %H:%M:%S')
        else:
            dic[c.name] = getattr(self, c.name)
    return dic


def list_to_json(self):
    lis = []
    for c in self:
        cct = to_json(c)
        lis.append(cct)
    return lis
