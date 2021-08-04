#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql
import json
import config


class MsqlTools:
    """mysql util"""
    db = None
    cursor = None

    def __init__(self):
        self.host = config.mysql_config['host']
        self.port = config.mysql_config['port']
        self.userName = config.mysql_config['userName']
        self.password = config.mysql_config['password']
        self.dbName = config.mysql_config['dbName']
        self.charsets = config.mysql_config['charsets']
        print("配置文件：" + json.dumps(config.mysql_config))

    # 链接数据库
    def get_con(self):
        """ 获取conn """
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.userName,
            passwd=self.password,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 主键查询数据
    def get_one(self, sql):
        res = None
        try:
            self.get_con()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print("查询失败！" + str(e))
        return res

    # 查询列表数据
    def get_all(self, sql):
        res = None
        try:
            self.get_con()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print("查询失败！" + str(e))
        return res

    # 插入数据
    def __insert(self, sql):
        count = 0
        try:
            self.get_con()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as e:
            print("操作失败！" + str(e))
            self.db.rollback()
        return count

    # 保存数据
    def save(self, sql):
        return self.__insert(sql)

    # 更新数据
    def update(self, sql):
        return self.__insert(sql)

    # 删除数据
    def delete(self, sql):
        return self.__insert(sql)


if __name__ == '__main__':
    """主程序入口"""
    dbUtil = MsqlTools()
    print("对象实例后的属性："+json.dumps(dbUtil.__dict__))

    # 主键查询
    sql = "select * from t_user"
    print("get_one执行结果：" + str(MsqlTools.get_one(dbUtil, sql)))

    # 列表查询
    sql = "select * from user where 1 = 1 "
    print("get_all执行结果：" + str(MsqlTools.get_all(dbUtil, sql)))

    # 插入
    sql = "INSERT INTO user(`id`, `name`) VALUES (8, 'admin');"
    print("save执行结果：" + str(MsqlTools.save(dbUtil, sql)))

    # 更新
    sql = "update user set name= 'admin1' where id =6 "
    print("update执行结果：" + str(MsqlTools.update(dbUtil, sql)))

    # 删除
    sql = "delete from user where id = 5"
    print("delete执行结果：" + str(MsqlTools.delete(dbUtil, sql)))
