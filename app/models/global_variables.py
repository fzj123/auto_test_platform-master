#!/usr/bin/python
# -*- coding:utf-8 -*-

import json


class GlobalVariables(object):
    '''单例对象，保存依赖数据'''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        self.globalVars = {}
        self.res = []


    def setVar(self,key,value):
        '''添加全局变量'''
        self.globalVars[key] = value
        print("当前全局变量：",self.globalVars)

    def getVar(self,key):
        '''获取某个全局变量'''
        return self.globalVars.get(key)

    def getVars(self):
        '''获取全部全局变量'''
        return self.globalVars

    def deleteVar(self,key):
        '''删除某个全局变量'''
        self.globalVars.pop(key)

    def cleanVars(self):
        '''清空全局变量'''
        self.globalVars.clear()

    def deleteVars(self):
        '''删除全局变量'''
        del self.globalVars

    def save_global_variable(self, globalVariable, res):
        '''保存被依赖数据到全局变量中'''
        import jsonpath
        for globalv in globalVariable.split(";"):
            g = globalv.strip()
            if g:
                key = g.split('=')[0].strip()
                value_expr = g.split('=')[1].strip()
                value = jsonpath.jsonpath(json.loads(res),value_expr)[0]  # 返回列表，取第一个
                self.setVar(key,value)
        self.getVars()  # 打印当前所有全局变量

    def save_variable(self, globalVariable):
        self.cleanVars()
        for globalv in globalVariable:
            key= globalv[0]
            valve= globalv[1]
            self.setVar(key,valve)


gv = GlobalVariables()

print(gv.globalVars)


if __name__ == '__main__':
    globalVariable = (('code', 'd41243a01aea'), ('authToken', '0d9d51cfeb9ef85416083fa4fb0832e3'))
    gv.save_variable(globalVariable)



