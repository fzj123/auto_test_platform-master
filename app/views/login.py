#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, session, jsonify, request
from functools import wraps
from app.models.log import Logzero
from app.db.db_user_list import db_user_list

mod = Blueprint('user', __name__,
                        template_folder='templates')

#========================登录模块开始====================================#
log = Logzero()
#设置登录认证
def authorize(fn):
    @wraps(fn)
    def wrapper():
        user = session.get('user', None)
        if user:
            log.info ("已登录")
            return fn()
        else:
            log.info ("未登录")
            return render_template("login.html")
    return wrapper


#登录页面
@mod.route('/login.html')
def login():
    return render_template("login.html")


#检查登录信息是否正确
@mod.route('/checklogin', methods=['GET'])
def checklogin():
    username = request.values.get("username")
    password = request.values.get("password")
    log.info('username : %s' %username)
    log.info('password : %s' %password)
    if username=='' or password=='':
        result = jsonify({'msg': '用户名或密码不能为空'})
    else:
        # 检查数据是否存在该用户
        list = db_user_list().check_login(username,password)
        if (len(list) > 0):
            result = jsonify({'msg': '登录成功'})
            # 登录成功设置会话
            session['user'] = list
        else:
            result = jsonify({'msg': '用户名或密码错误'})

    return result, {'Content-Type': 'application/json'}





#登出
@mod.route('/loginout')
def loginout():
    session['user']=None
    return render_template("login.html")