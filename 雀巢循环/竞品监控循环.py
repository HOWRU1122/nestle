# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/PycharmProjects/nestle/违规雷达/竞品监控首页.py")
apath2 = os.path.join(curpath, "/PycharmProjects/nestle/违规雷达/竞品监控品牌详情页.py")
apath3 = os.path.join(curpath, "/PycharmProjects/nestle/违规雷达/竞品监控店铺详情页.py")

print(apath1,apath2,apath3)
l = [apath1,apath2,apath3]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)
