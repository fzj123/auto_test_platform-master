#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
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


if __name__ == '__main__':

    s = db_user_list()
    a = s.show_user_list()
    c = len(a)
    print(a)
    print(c)
