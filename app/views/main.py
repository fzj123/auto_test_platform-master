#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template

mod = Blueprint('main', __name__,
                        template_folder='templates')

#主页
@mod.route('/main.html')
def main():
    return render_template("main.html")