#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from app.models.mysql_tools import MsqlTools



class db_items_list:

    def show_items_list(self,page,limit,sortOrder,itemsName):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if itemsName == '':
            sql = string.Template('select * from t_items order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            items = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_items;'
            sectors_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(sectors_list)
        else:
            sql = string.Template('select * from t_items WHERE items_name like "%$itemsName%" order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(itemsName=itemsName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            items = MsqlTools.get_all(dbUtil, sql)
            total = len(items)
        for i in range(len(items)):
            result = {}
            result['id'] = items[i][0]
            result['items_name'] = items[i][1]
            result['create_user'] = items[i][2]
            result['create_time'] = items[i][3]
            result['describes'] = items[i][4]

            results.append(result)

        return results, total

    def add_items(self,items_name,create_user,describes):
        """
        添加项目
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = uuid.uuid4()

        dbUtil = MsqlTools()
        sql = string.Template(
            'insert into t_items (id, items_name,create_user,create_time,describes) values ("$id","$items_name","$create_user","$create_time","$describes");')
        sql = sql.substitute(id=id, items_name=items_name, create_user=create_user, create_time=now_time, describes=describes)
        str = MsqlTools.save(dbUtil, sql)
        return str

    def edit_items(self,id,items_name,describes):
        """
        编辑用户
        :return:
        """

        dbUtil = MsqlTools()
        sql = string.Template(
            'update t_items set items_name= "$items_name", describes="$describes" where id ="$id";')
        sql = sql.substitute(id=id, items_name=items_name, describes=describes)
        result = MsqlTools.update(dbUtil, sql)
        return result

    def delete_items(self,itemsId):
        """
        删除项目
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'DELETE FROM t_items WHERE id ="$itemsId";')
        sql = sql.substitute(itemsId=itemsId)
        result = MsqlTools.delete(dbUtil, sql)

        return  result

    def items_name(self):
        """
        获取项目名称列表
        :return:
        """
        dbUtil = MsqlTools()

        sql = 'select items_name from t_items order by create_time asc;'
        items_name = MsqlTools.get_all(dbUtil, sql)
        result = []
        for i in items_name:
            result.append(i[0])
        return result


if __name__ == '__main__':

    s = db_items_list()
    a = s.edit_items('10','12345','11111')
    print(a)

