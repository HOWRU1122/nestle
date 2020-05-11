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

#打开医务泄露页面
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl/dd[3]/a").click()
sleep(1)

#打开竞品监控页面
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl/dd[2]/a").click()
sleep(1)

#打开本品监控页面
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl/dd/a").click()
sleep(1)

#打开本品列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd/a").click()
sleep(1)

#打开竞品列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd[2]/a").click()
sleep(1)

#打开医务泄露列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd[3]/a").click()
sleep(1)

#打开邮件信息
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd[4]/a").click()
sleep(1)

