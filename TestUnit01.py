from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 判断元素是否存在
def is_element_exist(xp):
    try: 
        if len(xp)==0:
            print("未找到Rquest Element")
            return False
        elif len(xp)==1:
            return True
        else:
            print("找到多个元素")
            return True
    except:
        return False

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
print("safe login ____________________>>>>>>>>>>>>>>>>>",datetime.now())
print(safeLoginBtn)
# 接下来测试是否可以WebDriverWait

try:
    
    # WebDriverWait(driver,30).until(lambda driver:driver.find_element_by_xpath('//*[@id="Pl_Core_UserInfo__6"]/div[2]/div[1]/div/a/span/'))
    WebDriverWait(driver,30,0.2).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"编辑个人资料")))
    # # print(driver.find_element_by_link_text("管理中心").id())
    # manager=driver.find_element_by_link_text("管理中心")
    # print(manager)
    print("Web Driver Login Success!!!!!!!!!!!!!!",datetime.now())
except:
    print("failed!!!!!!!!!!!!!",datetime.now())

# 执行下滑操作
# print(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"下一页")))
# 一直未找到就一直给我找
while is_element_exist(driver.find_elements_by_link_text("下一页"))==False:
    driver.execute_script('window.scrollTo(0,1000000);console.log("I am scrolling!!!")')



# while EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"下一页"))!=EC.WebElement:
#     driver.execute_script('window.scrollTo(0,1000000);console.log("I am scrolling!!!")')

# print(driver.find_element_by_partial_link_text("下一页"))
# 滑到底了 可以开始采集本页微博了




