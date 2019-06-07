from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://baidu.com')
inp=driver.find_element_by_xpath('//*[@id="u1"]/a[1]')

print(inp.text)
