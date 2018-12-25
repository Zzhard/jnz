import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/opt/drivers/chromedriver')
driver.get('http://ui.imdsx.cn/uitester')

driver.find_element_by_css_selector('#i1')


# 步长 1s 超时时间 10s




# 1、time 不是不让用，只允许代码调试的时候用
# 2、隐士等待 不常用
# 3、显示等待


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


ecDemo = EC.presence_of_element_located((By.ID,'i1'))
print(ecDemo)
WebDriverWait(driver,10,1).until(ecDemo)


