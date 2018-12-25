from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/uitester/')
js = 'window.scrollTo(0,0);' # 讲滚动条调制最上方
driver.execute_script(js)# 执行写好的js


# 课堂练习
# http://ui.imdsx.cn/uitester/ 点击新建标签页面，在新建标签页面的input中输入任意文案

driver.find_element_by_css_selector('[href="/new-index/"]').click()
handle = driver.window_handles[-1]
driver.switch_to.window(handle)
driver.find_element_by_css_selector('#newtag').send_keys('123123')

