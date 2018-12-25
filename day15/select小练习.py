from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/html/')
js = 'window.scrollTo(0,1800);' # 讲滚动条调到select出现的位置
driver.execute_script(js)# 执行写好的js

sele = driver.find_element_by_xpath('//select[1]')

from selenium.webdriver.support.select import Select
# select模块只支持 select元素
# Select(sele).select_by_value('4')

# by index 是从0 开始查
# Select(sele).select_by_index(2)