#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify, session
from app.db.db_items_list import db_items_list
from app.models.log import Logzero

mod = Blueprint('items_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

log = Logzero()

#项目管理页面
@mod.route('/system/items_list.html')
def items_list():
    return render_template("system/items_list.html")

@mod.route('/system/itemsList', methods=['GET'])
def items_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    itemsName = str(request.args.get('items_name'))

    result, total = db_items_list().show_items_list(page,limit,sortOrder,itemsName)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/system/addItems', methods=['POST'])
def add_items():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    items_name = data['items_name']
    describes = data['describes']

    list = session.get('user', None)
    username = list[0]["username"]
    print('登录名称：{0}'.format(username))

    log.info('sector_name：{0},describes：{1}'.format(items_name, describes))

    #数据库添加部门
    result = db_items_list().add_items(items_name,username,describes)

    if result == 1:
        code = 200
        message = 'add success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑项目
@mod.route('/system/editItems', methods=['POST'])
def edit_items():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    items_name = data['items_name']
    describes = data['describes']

    log.info('id：{0},sector_name：{1},items_name：{2}'.format(id,items_name,describes))

    #数据库更新项目
    result = db_items_list().edit_items(id,items_name,describes)

    if result == 1:
        code = 200
        message = 'deit success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result


#用户id删除项目
@mod.route('/system/deleteItems', methods=['GET'])
def delete_items():

    # 对参数进行操作
    itemsId = int(request.args.get('itemsId'))
    result = db_items_list().delete_items(itemsId)

    if result == 1:
        code = 200
        message = 'delete success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})

    return result

