#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from app.models.mysql_tools import MsqlTools



class db_user_list:

    def show_user_list(self,page,limit,sortOrder,loginName):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if loginName == '':
            sql = string.Template('select * from t_user order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            users = MsqlTools.get_all(dbUtil, sql)
            sql_total = 'select * from t_user;'
            user_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(user_list)
        else:
            sql = string.Template('select * from t_user WHERE user_name like "%$loginName%" order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(loginName=loginName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            users = MsqlTools.get_all(dbUtil, sql)
            total = len(users)
        for i in range(len(users)):
            result = {}
            result['id'] = users[i][0]
            result['login_name'] = users[i][1]
            result['user_name'] = users[i][3]
            result['department'] = users[i][4]
            result['phone'] = users[i][5]
            result['email'] = users[i][6]
            result['create_time'] = users[i][7]
            result['last_time'] =  users[i][8]
            result['status'] = users[i][9]

            results.append(result)


        return results, total

    def add_user(self,login_name,password,user_name,department,phone,email,status):
        """
        添加用户
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = uuid.uuid4()

        dbUtil = MsqlTools()
        sql = string.Template(
            'insert into t_user (id,login_name,password,user_name,department,phone,email,create_time,last_time,status) values ("$id","$login_name","$password","$user_name","$department","$phone","$email","$create_time","$last_time","$status");')
        sql = sql.substitute(id=id, login_name=login_name, password=password, user_name=user_name, department=department,
                             phone=phone, email=email, create_time=now_time, last_time=now_time, status=status)
        result = MsqlTools.save(dbUtil, sql)
        return result

    def edit_user(self,id,login_name,user_name,department,phone,email):
        """
        编辑用户
        :return:
        """

        dbUtil = MsqlTools()
        sql = string.Template(
            'update t_user set login_name= "$login_name", user_name="$user_name", department="$department", phone="$phone", email="$email" where id ="$id";')
        sql = sql.substitute(id=id, login_name=login_name, user_name=user_name, department=department,
                             phone=phone, email=email)
        result = MsqlTools.update(dbUtil, sql)
        return result


    def delete_user(self,userid):
        """
        删除用户
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'DELETE FROM t_user WHERE id ="$userid";')
        sql = sql.substitute(userid=userid)
        result = MsqlTools.delete(dbUtil, sql)

        return  result


    def check_login(self,username,password):
        """
        登录校验密码
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'SELECT id,login_name FROM t_user WHERE login_name = "$username" AND password = "$password";')
        sql = sql.substitute(username=username,password=password)
        list = MsqlTools.get_all(dbUtil, sql)
        results = []
        for i in range(len(list)):
            result = {}
            result['id'] = list[i][0]
            result['username'] = list[i][1]
            results.append(result)
        return results

    def user_name(self):
        """
        获取用户名称
        :return:
        """
        dbUtil = MsqlTools()

        sql = 'select user_name from t_user order by create_time asc;'
        sector_name = MsqlTools.get_all(dbUtil, sql)
        result = []
        for i in sector_name:
            result.append(i[0])
        return result

if __name__ == '__main__':

    s = db_user_list()
    a = s.user_name()
    print(a)

