from selenium import webdriver
from excelWT import write_excel

driver=webdriver.Chrome()
# driver.get("http://www.zhihu.com")
driver.get("https://weibo.com/5849524630/")

# driver.get('http://baidu.com')
# inp=driver.find_element_by_xpath('//*[@id="u1"]/a[1]')

# print(inp.text)
driver.implicitly_wait(15)
# texts =driver.find_elements_by_xpath('/')
texts='aaaa'
# print(len(texts))
# for t in texts:
#     print(t.text)
print(texts)
print('<<<<<<<<<<<done>>>>>>>>>>>')

# driver.find_element("id","ext-element-15").get_attribute("innerHTML")
# 获取div中的文本

print('success')