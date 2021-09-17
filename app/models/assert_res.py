#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jsonpath
import json
from collections import Counter

def assert_res(assertRes, res):
    res_status = 'PASS'
    s =  assertRes.split(";")
    for i in assertRes.split(";"):
        i_ = i.strip()
        if i_:
            actual_expr = i_.split("=")[0].strip()
            actual = jsonpath.jsonpath(json.loads(res), actual_expr)[0]
            expect = i_.split("=")[1].strip()
            if str(actual) != expect:
                res_status = 'FALSES'
                return res_status
    return res_status

def  parse_res(actual, res):

    actual = jsonpath.jsonpath(json.loads(res), actual)
    try:
        result = Counter(actual)
    except Exception as e:
        print('返回结果错误%s'%e)
        raise e
    return result

if __name__ == '__main__':
    res_status = assert_res('$..success=success;', '{"success":"success"}')
    print(res_status)
    a='{"code":"0","count":45,"dataSource":{"list":[{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626160248999","uuid":"000000000000000090aab7caf565fbfc"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626160247021","uuid":"00000000000000009f8f8fd1f85d6b34"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626160195620","uuid":"0000000000000000b4ecbaf7aef6926f"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626160142880","uuid":"000000000000000088bb818b66fa0944"},{"content":"开始自动运行","level":1,"mac":"d412438bd348","maxTime":"","time":"1626160141357","uuid":"0000000000000000a9f3c3b0266e834f"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159914871","uuid":"00000000000000008624e61d91c7f47c"},{"content":"切换为自动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159912759","uuid":"0000000000000000a11c7c8ebb046bb8"},{"content":"切换为手动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159911704","uuid":"0000000000000000a65854955f147c5f"},{"content":"切换为手动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159908625","uuid":"0000000000000000927aa101ed5970a1"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159882171","uuid":"0000000000000000a26535780a90952c"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159829487","uuid":"0000000000000000aeba2f36649a82cd"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159827469","uuid":"00000000000000009c492f142df16f1f"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159775953","uuid":"0000000000000000b759c740e195a77d"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159723267","uuid":"0000000000000000b30568b05da3bbb9"},{"content":"开始自动运行","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159721786","uuid":"00000000000000009e29816d4f12ae2d"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159690808","uuid":"0000000000000000b55b06e6d4d603e2"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159689145","uuid":"0000000000000000bbca7c3ef09888bc"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159687292","uuid":"00000000000000008724c7185daefb18"},{"content":"切换为自动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159685727","uuid":"0000000000000000b21704549a9de680"},{"content":"切换为手动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159681653","uuid":"000000000000000084d07b1a56d8034f"},{"content":"切换为手动模式","level":0,"mac":"d412438bd348","maxTime":"","time":"1626159159922","uuid":"00000000000000009d312a47a2536448"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626159007946","uuid":"000000000000000090d864135c274b38"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158955331","uuid":"00000000000000008a7c0e31d2d4f6fb"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158902461","uuid":"00000000000000009d7e44dc4cc7b657"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158900551","uuid":"00000000000000009b658a4bbf6a13d6"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158849092","uuid":"0000000000000000b01e759c9354781e"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158796392","uuid":"0000000000000000bd6c008be5cfbdd2"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158794459","uuid":"000000000000000080717452c866c185"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158742036","uuid":"00000000000000009d81e62025b550d1"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158689300","uuid":"000000000000000083aff00297cca78b"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158687321","uuid":"0000000000000000a3b0c6071256cf6e"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158635819","uuid":"00000000000000009ac60a100e47c62e"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158583083","uuid":"0000000000000000b4c5dc22c5b882d8"},{"content":"开始自动运行","level":1,"mac":"d412438bd348","maxTime":"","time":"1626158581544","uuid":"0000000000000000897d04a3122359c5"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626154147479","uuid":"0000000000000000b6de3b68c8c66a59"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626154095040","uuid":"0000000000000000b98a4654dfe65004"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626154042191","uuid":"00000000000000009dd58f62d40793e4"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626154040247","uuid":"0000000000000000aef4743e174d381f"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153988833","uuid":"00000000000000008891f34781167b9e"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153936095","uuid":"0000000000000000b08ae3f395fda7ee"},{"content":"到达标签0","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153934162","uuid":"00000000000000009e8c856d78eddae9"},{"content":"到达标签1","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153881720","uuid":"000000000000000086db8c890cf8c614"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153828952","uuid":"0000000000000000852990e7474e7ee3"},{"content":"到达标签2C","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153826984","uuid":"00000000000000008701b22683d5d800"},{"content":"到达标签2","level":1,"mac":"d412438bd348","maxTime":"","time":"1626153775465","uuid":"0000000000000000bc15fdb59a199394"}],"pageNum":1,"pageSize":1,"total":45},"errcode":"200","errmsg":"查询成功","msg":"查询成功","openId":"","totalRow":null}'
    b = json.dumps(a)
    res_text = parse_res('$..content', a)
    print(res_text)
