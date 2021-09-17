SECRET_KEY = 'you-will-never-guess'

#数据库配置
mysql_config = {
    "host": "localhost",
    "port": 3306,
    "userName": "root",
    "password": "123456",
    "dbName": "test_auto",
    "charsets": "UTF8"
}


# 目录相关配置
import os
currentPath = os.path.dirname(os.path.abspath(__file__))
logPath = os.path.join(currentPath,'logs')



