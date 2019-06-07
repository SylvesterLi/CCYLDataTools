from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

driver=webdriver.Chrome()
driver.get('https://weibo.com/5849524630/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop') # 获取百度页面
print(datetime.now())
print("DateTime______________>>>>>>>>>>>>>")
print(driver.page_source)

# 等待15秒 页面加载完毕
driver.implicitly_wait(15)

# 找到登录
loginBtn=driver.find_element_by_xpath('//*[@id="pl_common_top"]/div/div/div[3]/div[2]/ul/li[3]/a')
print("Login Btn____________INFO>>>>>>")
print(loginBtn)

loginBtn.click()

# 安全登录不能使用xpath 其//*[@id="layer_15599146676261"]/div[2]/div[3]/div[1]/a[2]中 id会变化
safeLoginBtn=driver.find_element_by_link_text("安全登录")
safeLoginBtn.click()
print("safe login ____________________>>>>>>>>>>>>>>>>>")
print(safeLoginBtn)

# 接下来测试是否可以WebDriverWait

