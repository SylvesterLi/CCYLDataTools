from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import  datetime
import time

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
print(datetime.now())
driver.get('https://weibo.com/5849524630/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop') # 获取百度页面
print(driver)
try:
    driver.implicitly_wait(15)
    print(driver)
    if driver.find_element_by_link_text("登录"):
        print("success!!!")
        input=driver.find_element_by_link_text("登录")
        input.click()
        try:
            login_safe=driver.find_element_by_link_text("安全登录")
            login_safe.click()
            driver.implicitly_wait(15)
            print("safe click")
        except:
            print("safe login failed!!!")
            
        # 此时页面加载完成可以等待异步页面元素
        # 可以开始登录
        
        print("回到我的主页")
        driver.implicitly_wait(15)
    if driver.find_element_by_partial_link_text("编辑个人资料"):
        action = Actions(driver)
        action.sendKeys(Keys.END)
        print("Edit found")
        action.sendKeys(Keys.END)
        driver.implicitly_wait(20)
        action.sendKeys(Keys.END)
        driver.implicitly_wait(20)
        action.sendKeys(Keys.END)
        print("往下滑了")
        driver.implicitly_wait(20)
        action.sendKeys(Keys.END)
        driver.implicitly_wait(20)
        action.sendKeys(Keys.END)
        driver.implicitly_wait(20)
        print("滑到底了")
    else:
        print("Edit Not Found")
        print("ready click next page")
    # 这一步有问题
    # WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_link_text("下一页"))
        
    # driver.get('http://baidu.com')
    
 
    # time.sleep(5)
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # time.sleep(2)
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # time.sleep(2)
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # element= WebDriverWait(driver,5,0.5).until(lambda driver:driver.find_element_by_link_text("下一页"))
    # input = driver.find_element_by_id('kw') #获取输入框
    try:
        
        driver.implicitly_wait(20)
        inp=driver.find_element_by_partial_link_text("下一页")
        inp.click()
        print("clicked!!!")
    except:
        print("not found Next Page")
        
except:
    print("Try Error上面崩了")
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


