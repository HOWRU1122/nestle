# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os

curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/雀巢循环/本品监控循环.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/雀巢循环/竞品监控循环.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/雀巢循环/医务泄露循环.py")
apath4 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/雀巢循环/配置信息循环.py")
apath5 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/雀巢循环/雀巢首页循环.py")

print(apath1,apath2,apath3,apath4,apath5)
l = [apath1,apath2,apath3,apath4,apath5]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)

