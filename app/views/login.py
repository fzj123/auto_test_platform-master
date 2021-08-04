#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

mod = Blueprint('user', __name__,
                        template_folder='templates')

#登录页面
@mod.route('/login')
def login():
    return render_template("login.html")