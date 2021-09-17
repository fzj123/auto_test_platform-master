#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from global_variables import gv
import re

def parameter_substitution(strParam):
    '''依赖参数值替换为实际值'''
    if strParam is None:
        return
    else:
        keys = re.findall('', strParam)
        for key in keys:
            value = gv.getVar(key)
            strParam = strParam.replace('${' + key + '}', str(value))  # replace返回替换后的新字符串
            print('替换参数化值后的字符串是：', strParam)
        return strParam

if __name__ == '__main__':
    strParam = parameter_substitution('authToken=${token}')
    print(type(strParam))
    print(strParam)
