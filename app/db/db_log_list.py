#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from flask import session

from app.models.mysql_tools import MsqlTools



class db_log_list:

    def show_log_list(self,page,limit,sortOrder,logName):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if logName == '':
            sql = string.Template('select * from t_log order by operation_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            items = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_log;'
            sectors_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(sectors_list)
        else:
            sql = string.Template('select * from t_log WHERE log_name like "%$logName%" order by operation_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(logName=logName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            items = MsqlTools.get_all(dbUtil, sql)
            total = len(items)
        for i in range(len(items)):
            result = {}
            result['id'] = items[i][0]
            result['log_name'] = items[i][1]
            result['operation_type'] = items[i][2]
            result['operation_user'] = items[i][3]
            result['sector_name'] = items[i][4]
            result['operation_status'] = items[i][5]
            result['operation_time'] = items[i][6]
            result['log_describes'] = items[i][7]

            results.append(result)

        return results, total

    def add_log(self, log_name, operation_type, operation_status, log_describes):
        """
        添加日志
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        list = session.get('user', None)
        operation_user = list[0]["username"]
        sector_name = self.sector_user(operation_user)
        id = uuid.uuid4()

        dbUtil = MsqlTools()
        sql = string.Template(
            'insert into t_log (id,log_name,operation_type,operation_user,sector_name,operation_status,operation_time,log_describes) values ("$id","$log_name","$operation_type","$operation_user","$sector_name","$operation_status","$operation_time","$log_describes");')
        sql = sql.substitute(id=id, log_name=log_name, operation_type=operation_type, operation_user=operation_user,
                             sector_name=sector_name, operation_status=operation_status, operation_time=now_time,
                             log_describes=log_describes)
        result = MsqlTools.save(dbUtil, sql)
        return result


    def sector_user(self, login_name):
        """
        登录名称查询所属部门
        :return:
        """
        dbUtil = MsqlTools()

        sql = 'select department from t_user WHERE login_name = "$login_name";'

        sql = string.Template(
            'select department from t_user WHERE login_name = "$login_name";')
        sql = sql.substitute(login_name=login_name)
        sector_name = MsqlTools.get_all(dbUtil, sql)
        result = sector_name[0][0]

        return result

if __name__ == '__main__':

    s = db_log_list()
    a = s.add_log('添加日志','添加','成功','1111111111111111')
    print(a)