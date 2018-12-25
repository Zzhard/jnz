from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/uitester/')

# # 获取浏览器的大小
# size = driver.get_window_size()
# print(size)
# # 设置浏览器的大小
# driver.set_window_size(200,200)
# 最大化
# driver.maximize_window()

# 截图
# driver.get_screenshot_as_file('aa.png')

# 执行js的
# driver.execute_script('js')

# # 关闭的是当前页面
# driver.close()
# 退出的是驱动
# driver.quit()
js = 'window.scrollTo(0,0);' # 讲滚动条调制最上方
driver.execute_script(js)# 执行写好的js
# import time
# time.sleep(1)
# driver.find_element_by_link_text('新建标签页面').click()
# # 获取当前浏览器所打开的全部tag标识
# print(driver.window_handles)
# # 获取当前浏览器的当前tag标识
# print(driver.current_window_handle)
# # driver.close() 关闭的是driver.current_window_handle对应的页面
#
#
# handles = driver.window_handles[-1]
# # 如果函数被划横线，代表你的函数已经不推荐使用，提供了更加方便的用法
# driver.switch_to_window(handles)
#
# from selenium.webdriver.remote.switch_to import SwitchTo
# driver.switch_to.window(handles)
# # SwitchTo(driver).window(handles)
#
# driver.close()
# import time
# driver.find_element_by_css_selector('#i1').send_keys('123123')
# time.sleep(1)
# driver.find_element_by_css_selector('#i1').clear()
#
# 勾选的checkbox
# on= driver.find_element_by_css_selector('#on')
# # 未勾选的checkbox
# off= driver.find_element_by_css_selector('#off')
#
# print(on.is_selected())
# print(off.is_selected())


# iframe 必须一层一层进入
# driver.switch_to.frame('top-frame')
# driver.find_element_by_css_selector('#newtag').send_keys('12312')
#
# driver.switch_to.frame('baidu-frame')
# driver.find_element_by_css_selector('#kw').send_keys('besttest')
# # 返回上一层
# driver.switch_to.parent_frame()
# driver.find_element_by_css_selector('#newtag').clear()
# # 直接返回默认层
# driver.switch_to.default_content()
# driver.find_element_by_css_selector('#i1').send_keys('123123')


# 做UI自动化需要关注 你的项目是否有需要切换tag的 是否有需要切换iframe的

# 处理alert
# driver.find_element_by_css_selector('#alert').click()
# import time
#
# time.sleep(2)
#
# # 点击确认
# driver.switch_to.alert.accept()
# driver.find_element_by_css_selector('#confirm').click()
# # 取消按钮
# driver.switch_to.alert.dismiss()


# select模块


# 浏览器级别的操作
# driver.refresh() 刷新

driver.find_element_by_css_selector('[href="http://www.imdsx.cn"]').click()
import time
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()

