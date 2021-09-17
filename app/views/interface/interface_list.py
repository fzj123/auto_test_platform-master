#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify, session

from app.db.db_envi_list import db_envi_list
from app.db.db_interface_list import db_interface_list
from app.db.db_log_list import db_log_list
from app.db.db_variables_list import db_variables_list
from app.models.global_variables import GlobalVariables
from app.models.log import Logzero

mod = Blueprint('interface_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

log = Logzero()

#接口管理页面
@mod.route('/interface/interface_list.html')
def interface_list():
    return render_template("interface/interface_list.html")

@mod.route('/interface/interfaceList', methods=['GET'])
def interface_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    interfaceListName = str(request.args.get('interfaceList_name'))

    result, total = db_interface_list().show_interface_list(page,limit,sortOrder,interfaceListName)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/interface/addInterface', methods=['POST'])
def add_interface():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('请求参数：{0}'.format(data))
    interface_name = data['interface_name']
    request_type = data['request_type']
    interface_path = data['interface_path']
    head = data['head']
    items_name = data['items_name']
    describes = data['describes']

    #数据库添加接口
    result = db_interface_list().add_interface(interface_name,request_type,interface_path,head,items_name,describes)

    if result == 1:
        code = 200
        message = 'add success!'
        db_log_list().add_log('接口管理，添加接口！', '添加', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('接口管理，添加接口！', '添加', '失败', message)
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑接口
@mod.route('/interface/editInterface', methods=['POST'])
def edit_interface():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    interface_name = data['interface_name']
    request_type = data['request_type']
    interface_path = data['interface_path']
    head = data['head']
    items_name = data['items_name']
    describes = data['describes']
    interface_request = data['interface_request']
    interface_header = data['interface_header']
    interface_parameter = data['interface_parameter']
    interface_assert = data['interface_assert']


    #数据库更新项目
    result = db_interface_list().edit_interface(id,interface_name,request_type,interface_path,head,items_name, describes, interface_request, interface_header, interface_parameter, interface_assert)

    if result == 1:
        code = 200
        message = 'deit success!'
        db_log_list().add_log('接口管理，编辑接口！', '编辑', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('接口管理，编辑接口！', '编辑', '失败', message)
    result = jsonify({'code': code, 'msg': message})
    return result


#根据id删除接口
@mod.route('/interface/deleteInterface', methods=['GET'])
def delete_interface():

    # 对参数进行操作
    interfaceId = request.args.get('interfaceId')

    result = db_interface_list().delete_interface(interfaceId)

    if result == 1:
        code = 200
        message = 'delete success!'
        db_log_list().add_log('接口管理，删除接口！', '删除', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('接口管理，删除接口！', '删除', '失败', message)
    result = jsonify({'code': code, 'msg': message})

    return result

#测试验证接口
@mod.route('/interface/runInterface', methods=['POST'])
def run_interface():

    # 对参数进行操作
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    items_name = data['items_name']

    #获取所属项目的全局变量
    variables = db_variables_list().select_variables(items_name)
    gv = GlobalVariables()
    gv.save_variable(variables)
    #获取所属项目的ip端口
    envi = db_envi_list().select_envi('接口测试',items_name)
    #获取所属项目的测试数据
    test_date = db_interface_list().select_interface(id)



    if test_date:
        code = 200
        message = 'delete success!'
        db_log_list().add_log('接口管理，测试接口！', '测试', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('接口管理，测试接口！', '测试', '失败', message)
    result = jsonify({'code': code, 'msg': message})

    return result