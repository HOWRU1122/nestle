from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep

options =webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
#打开网址
driver.get("http://47.111.14.225:30017/monitorPage/selfMonitor/shop")
sleep(2)

#打开医务泄露列表
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl[2]/dd[3]/a").click()
sleep(2)

#宝贝搜索
driver.find_element_by_xpath("//input[@placeholder='请输入宝贝名称搜索']").send_keys("超启能恩")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/button").click()
sleep(1)