#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from flask import session

from app.models.mysql_tools import MsqlTools



class db_variables_list:

    def show_variables_list(self,page,limit,sortOrder,variablesName):
        """
        查询t_variables表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if variablesName == '':
            sql = string.Template('select * from t_variables order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            variables = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_variables;'
            variables_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(variables_list)
        else:
            sql = string.Template('select * from t_variables WHERE variables_name like "%$variables_name%" order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(variables_name=variablesName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            variables = MsqlTools.get_all(dbUtil, sql)
            total = len(variables)
        for i in range(len(variables)):
            result = {}
            result['id'] = variables[i][0]
            result['variables_name'] = variables[i][1]
            result['variables_value'] = variables[i][2]
            result['items_name'] = variables[i][3]
            result['create_time'] = variables[i][4]
            result['describes'] = variables[i][5]

            results.append(result)

        return results, total

    def add_variables(self,variables_name,variables_value,items_name,describes):
        """
        添加公共参数
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = uuid.uuid4()


        dbUtil = MsqlTools()
        sql = string.Template(
            'INSERT INTO t_variables (id,variables_name, variables_value, items_name, create_time, describes) VALUES ("$id","$variables_name","$variables_value","$items_name","$create_time","$describes");')
        sql = sql.substitute(id=id, variables_name=variables_name, variables_value=variables_value,items_name=items_name,create_time=now_time, describes=describes)
        str = MsqlTools.save(dbUtil, sql)
        return str

    def edit_variables(self,id,variables_name,variables_value,items_name,describes):
        """
        编辑测试环境
        :return:
        """

        dbUtil = MsqlTools()
        sql = string.Template(
            'update t_variables set variables_name= "$variables_name", variables_value="$variables_value", items_name="$items_name", describes="$describes" where id ="$id";')
        sql = sql.substitute(id=id, variables_name=variables_name, variables_value=variables_value, items_name=items_name, describes=describes)
        result = MsqlTools.update(dbUtil, sql)
        return result

    def delete_variables(self,variablesId):
        """
        删除公共参数
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'DELETE FROM t_variables WHERE id ="$variablesId";')
        sql = sql.substitute(variablesId=variablesId)
        result = MsqlTools.delete(dbUtil, sql)

        return  result

    def select_variables(self,items_name):
        """
        查询公共参数
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'SELECT variables_name,variables_value FROM t_variables WHERE items_name = "$items_name";')
        sql = sql.substitute(items_name=items_name)
        result = MsqlTools.get_all(dbUtil, sql)

        return  result




if __name__ == '__main__':

    s = db_variables_list()
    a = s.select_variables('测试项目')
    b = type(a)
    print(b)

