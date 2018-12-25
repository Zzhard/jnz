from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/move/')



s = driver.find_element_by_css_selector('#dragger')
s1 = driver.find_element_by_css_selector('#dragger1')
s2 = driver.find_element_by_css_selector('#dragger2')
s3 = driver.find_element_by_css_selector('#dragger3')
t1 = driver.find_element_by_css_selector('#i1')
t2 = driver.find_element_by_css_selector('#i2')
t3 = driver.find_element_by_css_selector('#i3')
t4 = driver.find_element_by_css_selector('#i4')

from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).drag_and_drop(s,t1).drag_and_drop(s1,t2).drag_and_drop(s2,t3).drag_and_drop(s3,t4).perform()