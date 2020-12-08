import time
from selenium import webdriver


username = "13750856517" # 请替换成你的用户名
password = "YK941122" # 请替换成你的密码

driver = webdriver.Chrome() # 选择Chrome浏览器
driver.get(url='http://www.fanyigou.com') # 打开京东会员网站
time.sleep(2)


driver.find_element_by_class_name('login-btn').click()
time.sleep(2)

driver.find_element_by_id('login_phone').click()
driver.find_element_by_id('login_phone').send_keys(username)
time.sleep(2)
driver.find_element_by_id('login_psw').click()
driver.find_element_by_id('login_psw').send_keys(password)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/button").click()
time.sleep(1)