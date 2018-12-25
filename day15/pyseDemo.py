'''

一个创建计划的业务

有一个性别的选项 1代表男  2代表女


选男 保存这个计划

查看这个计划的时候发现性别的选项变成了女

看点击保存时，前端向后端发送的请求参数参数是男，数据库指定有一个sex的字段用于存储性别，这是后端的问题


后端返回给前端是男 但显示是女 这是前端问题





'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Pyse(object):
    def __init__(self, browser='chrome', driverpath=None):
        if browser.lower() == 'chrome':
            if driverpath:
                self.driver = webdriver.Chrome(driverpath)
            else:
                self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()

    def url(self, url):
        self.driver.get(url)

    def element_wait(self,css):
        if '=>' in css:
            by = css.split('=>')[0]
            value = css.split('=>')[1]
        else:
            print('参数有误')

        if by == 'css':
            WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.CSS_SELECTOR,value)))
        elif by == 'id':
            WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.ID, value)))
        else:
            print('必须输入的格式是 css=>#i1 ')




    def get_element(self, css):
        self.element_wait(css)
        if '=>' in css:
            by = css.split('=>')[0]
            value = css.split('=>')[1]
        else:
            print('参数有误')
        if by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'id':
            element = self.driver.find_element_by_id(value)

        return element

    # sendkeys()
    def type(self,css,value):
        element = self.get_element(css)
        element.send_keys(value)


if __name__ == '__main__':
    pyse = Pyse(driverpath='/usr/local/opt/drivers/chromedriver')
    pyse.url('http://ui.imdsx.cn/uitester')
    css = 'css=>#i1'
    pyse.type(css,'12123')