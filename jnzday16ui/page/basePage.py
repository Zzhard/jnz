'''

basepage中主要存放，业务的web元素定位


'''
from lib.pyse import Pyse

# 放的是一些共用的api
class Base(object):
    def __init__(self):
        self.pyse = Pyse('chrome')

    def open(self):
        self.pyse.open('http://zbox.imdsx.cn/user-login-Lw==.html')

    def quit(self):
        self.pyse.quit()
# 只放与登录操作有关的
class LoginPage(Base):
    def send_username(self):
        css = 'css=>#account'
        self.pyse.type(css,'admin')
    # 定位密码 和 登录按钮 并 调用调试一下

    def send_passwd(self):
        css = 'css=>input[name="password"]'
        self.pyse.type(css,'houyafan123')

    def login(self):
        css = 'css=>#submit'
        self.pyse.click(css)

    def check_login(self):
        css = 'css=>a[href="/user-logout.html"]'
        flag = self.pyse.wait_and_save_exception(css,'test_a_login')
        return flag

class MenuPage(LoginPage):
    def click_bug(self):
        css='css=>a[href="/bug/"]'
        self.pyse.click(css)

    def crt_bug(self):
        css= 'css=>a[href^="/bug-create-1-0-moduleID"]'
        self.pyse.click(css)

class CreateBug(MenuPage):
    def module(self):
        css1 = 'css=>#module_chosen'
        self.pyse.click(css1)
        css2 = 'css=>#module_chosen>div>ul>li[data-option-array-index="1"]'
        self.pyse.click(css2)
    def select_module(self):
        js = "document.getElementById('module').style.display='';document.getElementById('module').style.width='100px';"
        self.pyse.js(js)
        css = 'css=>#module'
        self.pyse.select_by_value(css,'3')


    def version(self):
        css1 = 'css=>#openedBuild_chosen'
        self.pyse.click(css1)
        css2 = 'css=>#openedBuild_chosen>div>ul>li[data-option-array-index="1"]'
        self.pyse.click(css2)

    def type(self):
        css = 'css=>#type'
        self.pyse.select_by_value(css, 'install')
    def os(self):
        css='css=>#os'
        self.pyse.select_by_value(css,'win7')
    def browser(self):
        css = 'css=>#browser'
        self.pyse.select_by_value(css,'ie')
    def date(self):
        css='css=>#deadline'
        self.pyse.type(css,'2018-12-20')

    def title(self):
        css='css=>#title'
        self.pyse.type(css,'dsx测试')

    def content(self):
        css1 = 'css=>.ke-edit-iframe'
        self.pyse.switch_to_frame(css1)
        css2 = 'css=>.article-content'
        self.pyse.clear(css2)
        self.pyse.type(css2,'test')
    def content2(self):
        js="document.getElementById('steps').style.display='';"
        self.pyse.js(js)
        css='css=>#steps'
        self.pyse.clear(css)
        self.pyse.type(css,'test1111')
    def content3(self):
        js = "document.getElementById('steps').style.display='';document.getElementById('steps').innerText='222222';"
        self.pyse.js(js)

    def save(self):
        self.pyse.switch_to_frame_out()
        css='css=>#submit'
        self.pyse.click(css)
    def check_createBug(self):
        css = 'css=>a[href^="/bug-create-1-0-moduleID"]'
        flag = self.pyse.wait_and_save_exception(css,'test_b_createBug')
        return flag

class Page(CreateBug):
    pass


if __name__ == '__main__':
    page = CreateBug()
    page.open()
    page.send_username()
    page.send_passwd()
    page.login()
    page.click_bug()
    page.crt_bug()
    page.module()
    page.version()
    # page.select_module()

    page.type()
    page.os()
    page.browser()
    page.date()
    page.title()
    page.content2()
    page.save()