#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify
from app.db.db_user_list import db_user_list

mod = Blueprint('user_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

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
    print(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)

@mod.route('/system/addUser', methods=['POST'])
def add_user():
    print(request.headers)
    data = request.get_json()
    print('返回结果：{0}'.format(data))
    login_name = data['login_name']
    password = data['password']
    user_name = data['user_name']
    department = data['department']
    phone = data['phone']
    email = data['email']
    print('login_name：{0},password：{1},user_name：{2},department：{3},phone：{4},email：{5}'.format(login_name, password,
                                                                                                user_name, department,
                                                                                                phone, email))

    #数据库添加用户
    db_user_list().add_user(login_name,password,user_name,department,phone,email,'1')

    result = jsonify({'code':200,'msg': '添加用户成功'})
    return result


@mod.route('/system/sectorNameList', methods=['POST'])
def sector_list():
    print(request.headers)
    result = db_user_list().sector_name()
    return_dict = {'rows': False}
    return_dict['rows'] = result

    return json.dumps(return_dict, ensure_ascii=False)



