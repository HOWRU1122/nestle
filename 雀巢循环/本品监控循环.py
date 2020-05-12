# -*- encoding=utf8 -*-
# !/usr/local/bin/python3.7
import os


curpath = os.path.dirname(os.path.realpath("__file__"))
apath1 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/违规雷达/本品监控首页.py")
apath2 = os.path.join(curpath, "/Users/yaokai/PycharmProjects/nestle/违规雷达/本品监控店铺详情页.py")

print(apath1,apath2)
l = [apath1,apath2]

for path in l:
    for i in range(1):
        os.system("python3 %s" % path)
