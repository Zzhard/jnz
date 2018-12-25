from selenium import webdriver
# 通过webdriver.chrome 创建浏览器 当做我们的服务端 会客户端进行ip端口绑定
#
# 我们的代码就是客户端
#
# 基于http协议发送 post请求


# 第三方包装在python的sit packages中
# pip install selenium
# 启动一个浏览器 浏览器就是我们的服务端
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
# 这里的url 必须带有http
driver.get('http://ui.imdsx.cn/uitester/')
# 8种单数定位方式
# id进行定位
# driver.find_element_by_id('i1').send_keys('123123')
# class 定位方式
# driver.find_element_by_class_name('classname').send_keys('123123')
# name定位方式
# driver.find_element_by_name('name').send_keys('123123')
# 文案定位
# driver.find_element_by_link_text('新建标签页面').click()
# 文案包含定位方式
js = 'window.scrollTo(0,0);' # 讲滚动条调制最上方
driver.execute_script(js)# 执行写好的js
# import time
# time.sleep(2)
# driver.find_element_by_partial_link_text('新建标签').click()
# 标签名定位 最不常用的
# driver.find_element_by_tag_name('input').send_keys('1111')
# xpath
# driver.find_element_by_xpath('//*[@id="i1"]').send_keys('2222')
# css id
# driver.find_element_by_css_selector('#i1').send_keys('2222')
# # css name
# driver.find_element_by_css_selector('name').send_keys()

# 8种复数定位方式 复数形式返回的都是一个列表
# element = driver.find_elements_by_id('i1')
# element[0].send_keys()

# 定位的元素如果元素下还有子元素，则可以通过元素进行再次定位
# 复数默认返回的都是列表，列表的顺序是按照html从上到下
elements = driver.find_elements_by_class_name('inner')
print(elements)
print(len(elements))
inputele = elements[0].find_elements_by_tag_name('input')
print(inputele)
inputele[0].send_keys('2222')

# 复数的留作作业 回家试一下
# driver.find_elements_by_css_selector()
# driver.find_elements_by_xpath()
# driver.find_elements_by_tag_name()
# driver.find_elements_by_link_text()
# driver.find_elements_by_partial_link_text()
# driver.find_elements_by_class_name()
# driver.find_elements_by_name()


# 最后两种
# driver.find_element_by_id()
# driver.find_element('id','i1')
# driver.find_elements()

