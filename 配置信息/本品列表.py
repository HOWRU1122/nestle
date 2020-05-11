from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
#打开网址
driver.get("http://47.111.14.225:30017/monitorPage/selfMonitor/shop")
sleep(1)
#打开本品列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd/a").click()
sleep(1)

#平台筛选
#选择淘宝
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[2]").click()
sleep(1)
#选择天猫
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[3]").click()
sleep(1)
#选择京东
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[4]").click()
sleep(1)
#选择全部
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li").click()
sleep(1)

#店铺搜索
driver.find_element_by_xpath("//input[@placeholder='请输入店铺名称搜索']").send_keys("雀巢")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/button").click()
sleep(1)

#查看详情
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div/a").click()
sleep(1)

#宝贝搜索
driver.find_element_by_xpath("//input[@placeholder='请输入宝贝名称搜索']").send_keys("超启能恩")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/button").click()
sleep(1)




