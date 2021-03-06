#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify
from app.db.db_sector_list import db_sector_list
from app.models.log import Logzero

mod = Blueprint('sector_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

log = Logzero()

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
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

#添加部门
@mod.route('/system/addSector', methods=['POST'])
def add_sector():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('请求参数：{0}'.format(data))
    sector_name = data['sector_name']
    describes = data['describes']

    log.info('sector_name：{0},describes：{1}'.format(sector_name, describes))

    #数据库添加部门
    result = db_sector_list().add_sector(sector_name,describes)

    if result == 1:
        code = 200
        message = 'add success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑部门
@mod.route('/system/editSector', methods=['POST'])
def edit_sector():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    sector_name = data['sector_name']
    describes = data['describes']

    log.info('id：{0},sector_name：{1},sector_name：{2}'.format(id,sector_name,describes))

    #数据库更新部门
    result = db_sector_list().edit_sector(id,sector_name,describes)

    if result == 1:
        code = 200
        message = 'deit success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result

#根据id删除部门
@mod.route('/system/deleteSector', methods=['GET'])
def delete_sector():

    # 对参数进行操作
    sectorid = request.args.get('sectorId')
    result = db_sector_list().delete_sector(sectorid)

    if result == 1:
        code = 200
        message = 'delete success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})

    return result

#查询所有部门
@mod.route('/system/sectorNameList', methods=['POST'])
def sector_lists():
    log.info('请求头：{0}'.format(request.headers))
    result = db_sector_list().sector_name()
    return_dict = {'rows': False}
    return_dict['rows'] = result

    return json.dumps(return_dict, ensure_ascii=False)




