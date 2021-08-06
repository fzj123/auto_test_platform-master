#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

mod = Blueprint('index', __name__,
                        template_folder='templates')

#主页
@mod.route('/index.html')
def index():
    return render_template("index.html")