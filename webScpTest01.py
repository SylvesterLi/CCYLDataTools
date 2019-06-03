from selenium import webdriver # 从selenium导入webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.baidu.com') # 获取百度页面

input = driver.find_element_by_id('kw') #获取输入框
searchButton = driver.find_element_by_id('su') #获取搜索按钮

input.send_keys("Python") #输入框输入"Python"
searchButton.click() #搜索

