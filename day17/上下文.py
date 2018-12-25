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
    # "appPackage":"com.tencent.mobileqq",
    "appPackage":"com.android.browser",
    # 入口
    # "appActivity":".Settings",
    # "appActivity":"com.tencent.mobileqq.activity.SplashActivity",
    "appActivity":".BrowserActivity",
    "noReset":True

}
# 默认appiumserver的服务端口是4723
# 参数1 链接服务的地址
# 参数2 链接服务的参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desc)

# print(driver.current_context)

# time.sleep(2)
# driver.find_element_by_id('com.android.browser:id/url').send_keys('http://ui.imdsx.cn/uitester')
# time.sleep(2)
# driver.press_keycode(66)
#
# print(driver.contexts)

# 切换webview 必须要求 开发将 webview的debug模式打开
# driver.switch_to.context('WEBVIEW_com.android.browser')
#
# driver.find_element_by_id('i1').send_keys(1111)
