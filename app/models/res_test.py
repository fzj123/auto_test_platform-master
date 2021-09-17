#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from app.models.assert_res import assert_res
from app.models.log import Logzero
import requests
from parameter_substitution import parameter_substitution
from global_variables import gv



log = Logzero()

class ResTest():
    def __init__(self, variables,envi,test_date):
        #获取请求数据
        self.test_date = test_date
        self.variables = variables
        self.envi = envi
      
    def res_test(self):
        """
        接口
        """


        log.info("==========【当前执行操作是：接口名称：%s：用例描述：%s】==========" %
             (self.test_date['interface_name'], self.test_date['describes']))
        log.info('ddt:{0}'.format(self.test_date))
        url = parameter_substitution(self.test_date['url'])
        params = parameter_substitution(self.test_date['params'])
        body = parameter_substitution(self.test_date['body']) 

        log.debug("> > > > >请求的url是：%s" % url)
        log.debug("> > > > >请求的method是：%s" % self.test_date['method'])
        log.debug("> > > > >请求的params是：%s" % params)
        log.debug("> > > > >请求的body是：%s" % body)
        log.debug("> > > > >断言内容assertRes是：%s" % self.test_date['assertRes'])
        log.debug("> > > > >请求的headers是：%s" % self.test_date['headers'])

     #转换成字符串
        headers_ = eval(self.test_date['headers'])
        
        if self.test_date['method'].upper() == 'POST':
            try:
                res = requests.post(url=url, headers=headers_,
                                    params=params, data=body, timeout=10)
                log.debug("执行请求后，结果是：%s" % res.text)
                if self.test_date['globalVariable']:
                    gv.save_global_variable(self.test_date['globalVariable'],res.text)

                # 断言
                if self.test_date['assertRes']:
                    res_status = assert_res(self.test_date['assertRes'], res.text)
                    log.debug("断言结果是：%s" % res_status)
            except Exception as e:
                log.debug('出错了，错误是%s' % e)
                raise e

        elif self.test_date['method'].upper() == 'GET':
            try:
                res = requests.get(url=url, headers=headers_,
                                    params=params, timeout=10)
                log.debug("执行请求后，结果是：%s" % res.text)
                if self.test_date['globalVariable']:
                    gv.save_global_variable(self.test_date['globalVariable'],res.text)
                # 断言
                if self.test_date['assertRes']:
                    res_status = assert_res(self.test_date['assertRes'], res.text)
                    log.debug("断言结果是：%s\n\n" % res_status)
            except Exception as e:
                log.debug('出错了，错误是%s' % e)
                raise e
            
        return res_status, res.text





if __name__ == '__main__':
 
    pass