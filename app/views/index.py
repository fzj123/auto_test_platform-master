#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, session
from app.views import login

mod = Blueprint('index', __name__,
                        template_folder='templates')

#主页
@mod.route('/index.html')
@login.authorize
def index():
    list = session.get('user', None)
    username = list[0]["username"]
    print('登录名称：{0}'.format(username))
    return render_template("index.html", message='Hello, %s' % username)