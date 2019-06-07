from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import  datetime
import time
import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
print(datetime.now())
driver.get('https://weibo.com/5849524630/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop') # 获取百度页面
print(driver.page_source)
try:
    driver.implicitly_wait(15)
    # try:
    #     remover=WebDriverWait(driver, 30, 0.2).until(
    #             lambda driver: driver.find_element_by_link_text("登录"))
    #     print("检测登录属性："+remover)
    # except:
    #     print("检测登录属性失败")
    
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
        except Exception as e:
            print("safe login failed!!!")
            print(traceback.print_exc())
        # 此时页面加载完成可以等待异步页面元素
        # 可以开始登录
        
        print("回到我的主页")
        driver.implicitly_wait(15)
    
    # 找到编辑资料
    text = driver.find_element_by_xpath('//*[@id="Pl_Core_UserInfo__6"]/div[2]/div[1]/div/a/span/text()')
    print(text)

    if driver.find_element_by_partial_link_text("编辑个人资料"):
        ActionChains(driver).send_keys(Keys.END)
        time.sleep(2)
        driver.execute_script("var q=document.documentElement.scrollTop=100000")
        print("滑了1下")
        driver.implicitly_wait(20)
        driver.execute_script("var q=document.documentElement.scrollTop=100000")
        print("滑了2下")
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
    except Exception as e:
        print("not found Next Page")
        # print(e.message)
        print(traceback.print_exc())
except Exception as e:
    print("Try Error上面崩了")
    print(datetime.now())
    print(traceback.print_exc())

    
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


