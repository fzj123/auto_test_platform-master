#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import json

from flask import Blueprint, render_template, request, jsonify, session
from app.db.db_log_list import db_log_list
from app.models.log import Logzero

mod = Blueprint('log_list', __name__,
                        template_folder='templates')



#时间格式转换
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

log = Logzero()

#日志管理页面
@mod.route('/system/log_list.html')
def log_list():
    return render_template("system/log_list.html")

@mod.route('/system/logList', methods=['GET'])
def log_list_query():

    return_dict= {'total': 0, 'rows': False}
    # 对参数进行操作
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    sortOrder = str(request.args.get('sortOrder'))
    log_name = str(request.args.get('log_name'))

    result, total = db_log_list().show_log_list(page,limit,sortOrder,log_name)
    len(result)
    return_dict['total'] = total
    return_dict['rows'] = result
    log.info(return_dict)

    return json.dumps(return_dict, ensure_ascii=False, cls=DateEncoder)


