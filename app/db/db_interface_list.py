#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time
import uuid

from flask import session

from app.models.mysql_tools import MsqlTools



class db_interface_list:

    def show_interface_list(self,page,limit,sortOrder,interfaceName):
        """
        查询t_interface表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if interfaceName == '':
            sql = string.Template('select * from t_interface order by last_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            interface = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_interface;'
            interface_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(interface_list)
        else:
            sql = string.Template('select * from t_interface WHERE interface_name like "%$interface_name%" order by last_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(interface_name=interfaceName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            interface = MsqlTools.get_all(dbUtil, sql)
            total = len(interface)
        for i in range(len(interface)):
            result = {}
            result['id'] = interface[i][0]
            result['interface_name'] = interface[i][1]
            result['items_name'] = interface[i][2]
            result['interface_status'] = interface[i][3]
            result['request_type'] = interface[i][4]
            result['head'] = interface[i][5]
            result['interface_path'] = interface[i][6]
            result['last_time'] = interface[i][7]
            result['interface_check'] = interface[i][8]
            result['describes'] = interface[i][9]
            result['interface_header'] = interface[i][10]
            result['interface_parameter'] = interface[i][11]
            result['interface_assert'] = interface[i][12]
            result['interface_request'] = interface[i][13]

            results.append(result)

        return results, total

    def add_interface(self,interface_name,request_type,interface_path,head,items_name,describes):
        """
        添加环境
        :return:
        """
        last_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        id = uuid.uuid4()

        dbUtil = MsqlTools()
        sql = string.Template(
            'INSERT INTO t_interface (id, interface_name, items_name, interface_status, request_type, head, interface_path, last_time, interface_check, describes) '
            'VALUES ("$id","$interface_name","$items_name","$interface_status","$request_type","$head","$interface_path","$last_time","$interface_check","$describes");')

        sql = sql.substitute(id=id, interface_name=interface_name, items_name=items_name, interface_status='', request_type=request_type, head=head, interface_path=interface_path, last_time=last_time, interface_check='', describes=describes)
        str = MsqlTools.save(dbUtil, sql)
        return str

    def edit_interface(self,id,interface_name,request_type,interface_path,head,items_name,describes,interface_request,interface_header,interface_parameter,interface_assert):
        """
        编辑测试环境
        :return:
        """

        dbUtil = MsqlTools()
        sql = string.Template(
            "update t_interface set interface_name= '$interface_name', request_type='$request_type', interface_path='$interface_path', head='$head', items_name='$items_name', describes='$describes', interface_request='$interface_request', interface_header='$interface_header', interface_parameter='$interface_parameter', interface_assert='$interface_assert' where id ='$id';")
        sql = sql.substitute(id=id, interface_name= interface_name, request_type=request_type, interface_path=interface_path, head=head, items_name=items_name, describes=describes, interface_request=interface_request, interface_header=interface_header, interface_parameter=interface_parameter, interface_assert=interface_assert)
        result = MsqlTools.update(dbUtil, sql)
        return result

    def delete_interface(self,interfaceId):
        """
        删除测试环境
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'DELETE FROM t_interface WHERE id ="$interfaceId";')
        sql = sql.substitute(interfaceId=interfaceId)
        result = MsqlTools.delete(dbUtil, sql)

        return  result

    def select_interface(self,id):
        """
        查询公共参数
        :return:
        """
        dbUtil = MsqlTools()
        sql = string.Template(
            'SELECT id,interface_name,describes,request_type,interface_path,interface_header,interface_parameter,interface_assert,interface_request FROM t_interface WHERE id = "$id";')
        sql = sql.substitute(id=id)
        interface = MsqlTools.get_all(dbUtil, sql)

        for i in range(len(interface)):
            result = {}
            result['id'] = interface[i][0]
            result['interface_name'] = interface[i][1]
            result['describes'] = interface[i][2]
            result['request_type'] = interface[i][3]
            result['interface_path'] = interface[i][4]
            result['interface_header'] = interface[i][5]
            result['interface_parameter'] = interface[i][6]
            result['interface_assert'] = interface[i][7]
            result['interface_request'] = interface[i][8]

        return  result






if __name__ == '__main__':

    s = db_interface_list()
    a = s.select_interface('bbb46bce-37e9-43b0-9d20-3e7a697ef852')
    print(a)

