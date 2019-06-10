from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 判断元素是否存在
def is_element_exist(xp):
    try: 
        if len(xp)==0:
            print("下一页Element未加载出来")
            return False
        elif len(xp)==1:
            return True
        else:
            print("找到多个元素")
            return True
    except:
        return False


# 生成网址
pageIndex=2
driver=webdriver.Chrome()
# 当前导航到第四页
driver.get('https://weibo.com/p/1001062321615032/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=%d#feedtop' % pageIndex)
# driver.get('https://weibo.com/5849524630/profile?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=4#feedtop')
# 打印时间
print(datetime.now())
print("DateTime______________>>>>>>>>>>>>>")
# print(driver.page_source)

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
    # 个人选择“编辑个人资料，官博选择“编辑微博” 此处存在js 检测不到
    # 换成检测搜索文本框 偶然情况下是会通过，但是没有关系 这里不再验证是否为自己账号，只做页面加载情况验证
    WebDriverWait(driver,40,0.2).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"青春湖北")))
    # 等待成功 未找到元素或者扫码时间过长就会报错
    print("Web Driver Login Success!!!!!!!!!!!!!!",datetime.now())
except:
    print("failed!!!!!!!!!!!!!",datetime.now())

# 执行下滑操作
# 一直未找到就一直给我找
# 经过验证此循环没有问题
# 会有较长时间卡顿
while is_element_exist(driver.find_elements_by_link_text("下一页"))==False:
    driver.execute_script('window.scrollTo(0,1000000);console.log("I am scrolling!!!")')

print("已找到最后一页，已到达底部")
driver.execute_script('window.scrollTo(0,1000000);console.log("I am scrolling!!!")')

# 表明当前页面已经加载完毕，可以开始读取所有节点
# 这是哪一页


# xpath 比较
# //*[@id="Pl_Official_MyProfileFeed__25"]/div/div[3]
# //*[@id="Pl_Official_MyProfileFeed__25"]/div/div[3]/div[2]/div/ul/li[1]/a/span/span/i/text()
# //*[@id="Pl_Official_MyProfileFeed__25"]/div/div[4]/div[2]/div/ul/li[1]/a/span/span/i

# i从1开始计数
# 第几页 还没确定变量 第i条
# 先确定循环
i=2

# 简单粗暴 直接看出总数是45 能跑就行
while i<=46:
    i=i+1
    print('第'+str(pageIndex)+'页第'+str(i)+'条：')
    print(driver.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__25"]/div/div[%d]/div[2]/div/ul/li[1]/a/span/span/i' % i).text)

print("<<<<<<done>>>>>>>")


# //*[@id="Pl_Official_MyProfileFeed__25"]/div/div[12]/div[1]/div[3]/div[4]
# 其中12为第几个div 投票、文章、原创 均没有问题



