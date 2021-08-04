#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request
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
    result = db_user_list().show_user_list()
    len(result)
    return_dict['total'] = len(result)
    return_dict['rows'] = result


    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)







