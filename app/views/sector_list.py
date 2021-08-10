#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify
from app.db.db_sector_list import db_sector_list

mod = Blueprint('sector_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

#部门管理页面
@mod.route('/system/sector_list.html')
def sector_list():
    return render_template("system/sector_list.html")

@mod.route('/system/sectorList', methods=['GET'])
def sector_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    sectorName = str(request.args.get('sector_name'))

    result, total = db_sector_list().show_sector_list(page,limit,sortOrder,sectorName)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    print(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/system/sectorUser', methods=['POST'])
def add_sector():
    print(request.headers)
    data = request.get_json()
    print('返回结果：{0}'.format(data))
    sector_name = data['sector_name']
    describes = data['describes']

    print('sector_name：{0},describes：{1}'.format(sector_name, describes))

    #数据库添加部门
    db_sector_list().add_sector(sector_name,describes)

    result = jsonify({'code':200,'msg': '添加用户成功'})
    return result






