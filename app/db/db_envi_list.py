#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from app.models.mysql_tools import MsqlTools



class db_envi_list:

    def show_envi_list(self,page,limit,sortOrder,enviName):
        """
        查询t_envi表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if enviName == '':
            sql = string.Template('select * from t_envi order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            envi = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_envi;'
            envi_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(envi_list)
        else:
            sql = string.Template('select * from t_envi WHERE envi_name like "%$enviName%" order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(enviName=enviName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            envi = MsqlTools.get_all(dbUtil, sql)
            total = len(envi)
        for i in range(len(envi)):
            result = {}
            result['id'] = envi[i][0]
            result['envi_name'] = envi[i][1]
            result['url'] = envi[i][2]
            result['port'] = envi[i][3]
            result['test_type'] = envi[i][4]
            result['items_name'] = envi[i][5]
            result['create_user'] = envi[i][6]
            result['create_time'] = envi[i][7]
            result['describes'] = envi[i][8]

            results.append(result)

        return results, total

    def add_envi(self,envi_name,url,port,test_type,items_name,create_user,describes):
        """
        添加环境
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = uuid.uuid4()

        dbUtil = MsqlTools()
        sql = string.Template(
            'INSERT INTO t_envi (id, envi_name, url, port, test_type, items_name, create_user, create_time, describes) VALUES ("$id","$envi_name","$url","$port","$test_type","$items_name","$create_user","$create_time","$describes");')
        sql = sql.substitute(id=id, envi_name=envi_name, url=url, port=port,test_type=test_type,items_name=items_name,create_user=create_user, create_time=now_time, describes=describes)
        str = MsqlTools.save(dbUtil, sql)
        return str

    def edit_envi(self,id,envi_name,url,port,test_type,items_name,describes):
        """
        编辑测试环境
        :return:
        """

        dbUtil = MsqlTools()
        sql = string.Template(
            'update t_envi set envi_name= "$envi_name", url="$url", port="$port", test_type="$test_type", items_name="$items_name", describes="$describes" where id ="$id";')
        sql = sql.substitute(id=id, envi_name=envi_name, url=url, port=port, test_type=test_type, items_name=items_name, describes=describes)
        result = MsqlTools.update(dbUtil, sql)
        return result

    def delete_envi(self,enviId):
        """
        删除测试环境
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'DELETE FROM t_envi WHERE id ="$enviId";')
        sql = sql.substitute(enviId=enviId)
        result = MsqlTools.delete(dbUtil, sql)

        return  result


    def select_envi(self,test_type,items_name):
        """
        查询测试环境
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'select url,port FROM t_envi WHERE test_type ="$test_type" and items_name="$items_name";')
        sql = sql.substitute(test_type=test_type,items_name=items_name)
        envi = MsqlTools.get_all(dbUtil, sql)

        for i in range(len(envi)):
            result = {}
            result['url'] = envi[i][0]
            result['port'] = envi[i][1]

        return  result






if __name__ == '__main__':

    s = db_envi_list()
    a = s.select_envi('接口测试','测试项目')
    print(a)

