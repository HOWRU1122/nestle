from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from time import sleep
import unittest
from selenium.webdriver import ActionChains

options = webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://td2.qingbaomofang.com/dashboard/market")
sleep(1)
#打开品牌列表
# 宝贝监控
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/div").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/ul/div/li[5]/ul/li/ul/li[3]/span").click()
sleep(3)
# 获取表格数据
tablemoney=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[8]/td[5]/div/span")
action = ActionChains(driver)
ActionChains(driver).move_to_element(tablemoney).perform()
sleep(1)
tabledaymoney = driver.find_element_by_xpath("/html/body/div[3]/div[2]").get_attribute("textContent")

print(tabledaymoney)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("com.tencent.mm:id/l2").click()
