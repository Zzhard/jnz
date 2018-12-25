from pyapp import Pyapp

from appium import webdriver
import time

desc = {
    # 手机唯一标示
    "deviceName":"127.0.0.1:62001",
    # 手机类型
    "platformName":"Android",
    # 手机的版本
    "platformVersion":"4.4.2",
    # 包名
    # "appPackage":"com.android.settings",
    "appPackage":"com.tencent.mobileqq",
    # "appPackage":"com.android.browser",
    # 入口
    # "appActivity":".Settings",
    "appActivity":"com.tencent.mobileqq.activity.SplashActivity",
    # "appActivity":".BrowserActivity",
    "noReset":True

}
# 默认appiumserver的服务端口是4723
# 参数1 链接服务的地址
# 参数2 链接服务的参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desc)

pyapp = Pyapp(driver)
css = 'id=>com.tencent.mobileqq:id/btn_login'
pyapp.click(css)
css = 'content=>请输入QQ号码或手机或邮箱'
pyapp.type(css,'123123')
css = 'content=>密码 安全'
pyapp.type(css,'123123')
css='content=>登录'
pyapp.click(css)