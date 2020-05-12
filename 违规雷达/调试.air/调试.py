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
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl/dd[2]/a").click()
sleep(1)
#查看品牌详情
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[9]/div/a").click()
sleep(1)
#查看店铺详情
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[8]/div/a").click()
sleep(1)
#查看违规截图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[7]/div/a").click()
sleep(1)
driver.find_element_by_xpath("//a[@href='http://itemscreenshot.oss-cn-hangzhou.aliyuncs.com/2020-05%2Fsku_tmall_613095401943_1589259140.png']").click()
sleep(1)

driver.switch_to_new_tab()

driver.switch_to_previous_tab()

