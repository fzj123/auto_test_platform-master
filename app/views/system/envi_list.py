#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify, session
from app.db.db_envi_list import db_envi_list
from app.models.log import Logzero

mod = Blueprint('envi_list', __name__,
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
@mod.route('/system/envi_list.html')
def envi_list():
    return render_template("system/envi_list.html")

@mod.route('/system/enviList', methods=['GET'])
def envi_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    enviListName = str(request.args.get('enviList_name'))

    result, total = db_envi_list().show_envi_list(page,limit,sortOrder,enviListName)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/system/addEnvi', methods=['POST'])
def add_envi():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('请求参数：{0}'.format(data))
    envi_name = data['envi_name']
    url = data['url']
    port = data['port']
    test_type = data['test_type']
    items_name = data['items_name']
    describes = data['describes']

    list = session.get('user', None)
    create_user = list[0]["username"]
    print('登录名称：{0}'.format(create_user))

    #数据库添加部门
    result = db_envi_list().add_envi(envi_name,url,port,test_type,items_name,create_user,describes)

    if result == 1:
        code = 200
        message = 'add success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑项目
@mod.route('/system/editEnvi', methods=['POST'])
def edit_items():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    envi_name = data['envi_name']
    url = data['url']
    port = data['port']
    test_type = data['test_type']
    items_name = data['items_name']
    describes = data['describes']


    #数据库更新项目
    result = db_envi_list().edit_envi(id,envi_name,url,port,test_type,items_name,describes)

    if result == 1:
        code = 200
        message = 'deit success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result


#用户id删除项目
@mod.route('/system/deleteEnvi', methods=['GET'])
def delete_items():

    # 对参数进行操作
    enviId = request.args.get('enviId')

    result = db_envi_list().delete_envi(enviId)

    if result == 1:
        code = 200
        message = 'delete success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})

    return result

