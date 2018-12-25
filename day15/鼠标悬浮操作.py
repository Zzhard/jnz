from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/uitester/')
js = 'window.scrollTo(0,0);'
driver.execute_script(js)

# element = driver.find_element_by_css_selector('#dis1')
#
# #  判断元素是否可见，可见返回true  不可见返回false
# print(element.is_displayed())
#
# element.click()

from selenium.webdriver.common.action_chains import ActionChains
# 先定位到鼠标要悬浮的那个元素
a = driver.find_element_by_css_selector('#a')
dis1 = driver.find_element_by_css_selector('#dis1')
# 然后通过鼠标操作，移动到这个元素上，在进行点击
ActionChains(driver).move_to_element(a).click(dis1).perform()




