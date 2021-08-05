#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time

from app.models.mysql_tools import MsqlTools



class db_user_list:

    def show_user_list(self):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        sql = 'select * from t_user;'
        users = MsqlTools.get_all(dbUtil, sql)
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

        return results

    def add_user(self,login_name,password,user_name,department,phone,email,status):
        """
        添加用户
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        dbUtil = MsqlTools()
        sql = string.Template(
            'insert into t_user (login_name,password,user_name,department,phone,email,create_time,last_time,status) values ("$login_name","$password","$user_name","$department","$phone","$email","$create_time","$last_time","$status");')
        sql = sql.substitute(login_name=login_name, password=password, user_name=user_name, department=department,
                             phone=phone, email=email, create_time=now_time, last_time=now_time, status=status)
        str = MsqlTools.save(dbUtil, sql)
        return str


if __name__ == '__main__':

    s = db_user_list()
    a = s.add_user('test05','123456','测试用户03','测试部门','13123223','1585813232@qq.com','1')
    print(a)

