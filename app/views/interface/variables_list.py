#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify, session
from app.db.db_variables_list import db_variables_list
from app.models.log import Logzero

mod = Blueprint('variables_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

log = Logzero()

#参数管理页面
@mod.route('/interface/variables_list.html')
def variables_list():
    return render_template("interface/variables_list.html")

@mod.route('/interface/variablesList', methods=['GET'])
def variables_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    variablesListName = str(request.args.get('variablesList_name'))

    result, total = db_variables_list().show_variables_list(page,limit,sortOrder,variablesListName)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/interface/addvariables', methods=['POST'])
def add_variables():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('请求参数：{0}'.format(data))
    variables_name = data['variables_name']
    variables_value = data['variables_value']
    items_name = data['items_name']
    describes = data['describes']

    #数据库添公共参数
    result = db_variables_list().add_variables(variables_name,variables_value,items_name,describes)

    if result == 1:
        code = 200
        message = 'add success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑项目
@mod.route('/interface/editvariables', methods=['POST'])
def edit_items():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    variables_name = data['variables_name']
    variables_value = data['variables_value']
    items_name = data['items_name']
    describes = data['describes']


    #数据库更新项目
    result = db_variables_list().edit_variables(id,variables_name,variables_value,items_name,describes)

    if result == 1:
        code = 200
        message = 'deit success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})
    return result


#根据id删除公共参数
@mod.route('/interface/deletevariables', methods=['GET'])
def delete_items():

    # 对参数进行操作
    variablesId = request.args.get('variablesId')


    result = db_variables_list().delete_variables(variablesId)

    if result == 1:
        code = 200
        message = 'delete success!'
    else:
        code = 500
        message = 'please try again!'
    result = jsonify({'code': code, 'msg': message})

    return result

