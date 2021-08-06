#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time

from app.models.mysql_tools import MsqlTools



class db_sector_list:

    def show_sector_list(self):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        sql = 'select * from t_sector;'
        sectors = MsqlTools.get_all(dbUtil, sql)
        for i in range(len(sectors)):
            result = {}
            result['id'] = sectors[i][0]
            result['sector_name'] = sectors[i][1]
            result['member'] = sectors[i][2]
            result['create_time'] = sectors[i][3]
            result['describes'] = sectors[i][4]

            results.append(result)

        return results

    def add_sector(self,sector_name,describes):
        """
        添加用户
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        dbUtil = MsqlTools()
        sql = string.Template(
            'insert into t_sector (sector_name,member,create_time,describes) values ("$sector_name","$member","$create_time","$describes");')
        sql = sql.substitute(sector_name=sector_name, member=0, create_time=now_time, describes=describes)
        str = MsqlTools.save(dbUtil, sql)
        return str


if __name__ == '__main__':

    s = db_sector_list()
    a = s.add_sector('测试部门','测试部门')
    print(a)

