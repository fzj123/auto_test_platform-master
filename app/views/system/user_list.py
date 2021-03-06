#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify
from app.db.db_user_list import db_user_list
from app.db.db_log_list import db_log_list
from app.models.log import Logzero

mod = Blueprint('user_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)
log = Logzero()

#用户管理页面
@mod.route('/system/user_list.html')
def user_list():
    return render_template("system/user_list.html")

@mod.route('/system/userList', methods=['GET'])
def user_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    user_name = str(request.args.get('user_name'))

    result,total = db_user_list().show_user_list(page,limit,sortOrder,user_name)

    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

#添加用户
@mod.route('/system/addUser', methods=['POST'])
def add_user():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('请求参数：{0}'.format(data))
    login_name = data['login_name']
    password = data['password']
    user_name = data['user_name']
    department = data['department']
    phone = data['phone']
    email = data['email']
    log.info('login_name：{0},password：{1},user_name：{2},department：{3},phone：{4},email：{5}'.format(login_name, password,
                                                                                                user_name, department,
                                                                                                phone, email))

    #数据库添加用户
    result = db_user_list().add_user(login_name,password,user_name,department,phone,email,'1')

    if result == 1:
        code = 200
        message = 'delete success!'
        db_log_list().add_log('系统管理，用户管理添加用户','添加','成功',message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('系统管理，用户管理添加用户', '添加', '失败', message)
    result = jsonify({'code': code, 'msg': message})
    return result

#编辑用户
@mod.route('/system/editUser', methods=['POST'])
def edit_user():
    log.info('请求头：{0}'.format(request.headers))
    data = request.get_json()
    log.info('返回结果：{0}'.format(data))
    id = data['id']
    login_name = data['login_name']
    user_name = data['user_name']
    department = data['department']
    phone = data['phone']
    email = data['email']
    log.info('login_name：{0},password：{1},user_name：{2},department：{3},phone：{4},email：{5}'.format(id,login_name,
                                                                                                user_name, department,
                                                                                                phone, email))

    #数据库添加用户
    result = db_user_list().edit_user(id,login_name,user_name,department,phone,email)

    if result == 1:
        code = 200
        message = 'deit success!'
        db_log_list().add_log('系统管理，用户管理编辑用户', '编辑', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('系统管理，用户管理编辑用户', '编辑', '失败', message)
    result = jsonify({'code': code, 'msg': message})
    return result


#根据id删除用户
@mod.route('/system/deleteUser', methods=['GET'])
def delete_user():

    # 对参数进行操作
    user_id = request.args.get('userId')

    result = db_user_list().delete_user(user_id)

    if result == 1:
        code = 200
        message = 'delete success!'
        db_log_list().add_log('系统管理，用户管理删除用户', '删除', '成功', message)
    else:
        code = 500
        message = 'please try again!'
        db_log_list().add_log('系统管理，用户管理删除用户', '删除', '失败', message)
    result = jsonify({'code': code, 'msg': message})
    return result

#查询所有用户
@mod.route('/system/userNameList', methods=['POST'])
def user_lists():
    log.info('请求头：{0}'.format(request.headers))
    result = db_user_list().user_name()
    return_dict = {'rows': False}
    return_dict['rows'] = result

    return json.dumps(return_dict, ensure_ascii=False)

