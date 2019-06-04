from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import  datetime
import time

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
print(datetime.now())
driver.get('https://weibo.com/5849524630/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop') # 获取百度页面
try:
    # driver.get('http://baidu.com')
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    element= WebDriverWait(driver,5,0.5).until(lambda driver:driver.find_element_by_link_text("下一页"))
    # input = driver.find_element_by_id('kw') #获取输入框
    

    input=driver.find_element_by_link_text("下一页")
    input.click()


    
finally:
    print("Error")
    print(datetime.now())
# searchButton = driver.find_element_by_id('su') #获取搜索按钮

# input.send_keys("Python") #输入框输入"Python"
# searchButton.click() #搜索

# 等待id为Pl_Official_MyProfileFeed__20的div出现



# input=driver.find_element_by_id('Pl_Official_MyProfileFeed__20')



# 滑到最下面才出现下一页 但是可能还是加载  还要检测下一页是否出现


# 这时候再进行检测
# https://weibo.com/5849524630/profile?pids=Pl_Official_MyProfileFeed__20&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=4#feedtop
# 其中page可控制
# 

# find 阅读xx次


