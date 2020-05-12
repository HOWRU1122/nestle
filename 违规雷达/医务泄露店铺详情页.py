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
#打开医务泄露页
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div/div/dl/dd[3]/a").click()
sleep(1)
#查看详情
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div/a").click()
sleep(1)

#时间选择
driver.find_element_by_xpath("//input[@placeholder='选择周']").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/table/tbody/tr[3]/td[4]/div/span").click()
sleep(1)

#段位选择
#选择一段
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[2]").click()
sleep(1)
#选择2段
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[3]").click()
sleep(1)
#选择全部
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li").click()
sleep(1)

#选择违规状态
#选择已违规
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[2]").click()
sleep(1)
#选择未违规
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[3]").click()
sleep(1)
#选择全部
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li").click()
sleep(1)

#导出
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/button/span").click()
#sleep(1)

#搜索
driver.find_element_by_xpath("//input[@placeholder='请输入宝贝名称搜索']").send_keys("超启能恩")
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div/button").click()
sleep(1)

#查看违规截图
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[6]/div/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/table/tbody/tr/td[2]/div/div//a[@class = 'candy-a-link']").click()
sleep(1)
driver.switch_to_new_tab()
driver.close()
sleep(1)
driver.switch_to_previous_tab()
sleep(1)



