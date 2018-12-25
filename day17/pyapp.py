from pyse import Pyse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
class Pyapp(Pyse):
    def __init__(self, driver):
        self.d = driver
        # 仅为了开下下面代码 有代码提示而引入，正式使用需要注释
        # from appium import webdriver
        # self.d = webdriver.Remote()

    def swipe_up(self):
        size = self.d.get_window_size()
        width = size.get('width')
        height = size.get('height')
        x = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.2
        self.d.swipe(x, y1, x, y2)

    def swipe_down(self):
        pass

    def swipe_left(self):
        pass

    def swipe_right(self):
        pass

    def element_wait(self, css, secs=5):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.ID, value)))
        elif by == "name":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.NAME, value)))
        elif by == "class":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.CSS_SELECTOR, value)))
        elif by == "android":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, value)))
        elif by == "content":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        '''
        Judge element positioning way, and returns the element.
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.d.find_element_by_id(value)
        elif by == "name":
            element = self.d.find_element_by_name(value)
        elif by == "class":
            element = self.d.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.d.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.d.find_element_by_xpath(value)
        elif by == "css":
            element = self.d.find_element_by_css_selector(value)
        elif by == "android":
            element = self.d.find_element_by_android_uiautomator(value)
        elif by == "content":
            element = self.d.find_element_by_accessibility_id(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

