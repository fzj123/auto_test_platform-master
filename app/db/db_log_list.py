#!/usr/bin/python
# -*- coding:utf-8 -*-

import string
import time

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


