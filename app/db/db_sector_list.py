#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time

from app.models.mysql_tools import MsqlTools



class db_sector_list:

    def show_sector_list(self,page,limit,sortOrder,sectorName):
        """
        查询t_user表所有数据
        """
        results = []
        dbUtil = MsqlTools()
        pageNo = (page - 1) * limit
        if sectorName == '':
            sql = string.Template('select * from t_sector order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            sectors = MsqlTools.get_all(dbUtil, sql)

            sql_total = 'select * from t_sector;'
            sectors_list = MsqlTools.get_all(dbUtil, sql_total)
            total = len(sectors_list)
        else:
            sql = string.Template('select * from t_sector WHERE sector_name like "%$sectorName%" order by create_time $sortOrder limit $pageNo,$limit;')
            sql = sql.substitute(sectorName=sectorName, pageNo=pageNo, limit=limit, sortOrder=sortOrder)
            sectors = MsqlTools.get_all(dbUtil, sql)
            total = len(sectors)
        for i in range(len(sectors)):
            result = {}
            result['id'] = sectors[i][0]
            result['sector_name'] = sectors[i][1]
            result['member'] = sectors[i][2]
            result['create_time'] = sectors[i][3]
            result['describes'] = sectors[i][4]

            results.append(result)

        return results, total

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

    def sector_name(self):
        """
        获取部门名称列表
        :return:
        """
        dbUtil = MsqlTools()

        sql = 'select sector_name from t_sector order by create_time asc;'
        sector_name = MsqlTools.get_all(dbUtil, sql)
        result = []
        for i in sector_name:
            result.append(i[0])
        return result



if __name__ == '__main__':

    s = db_sector_list()
    a = s.sector_name()
    print(a)

