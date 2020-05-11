# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/雀巢/配置信息/本品列表.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/雀巢/配置信息/竞品列表.py")
apath3 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/雀巢/配置信息/医务泄露列表.py")

print(apath1,apath2,apath3)
l = [apath1,apath2,apath3]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)
