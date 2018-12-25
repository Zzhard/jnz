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
    # 入口
    # "appActivity":".Settings"
    "appActivity":"com.tencent.mobileqq.activity.SplashActivity",
    "noReset":True

}
# 默认appiumserver的服务端口是4723
# 参数1 链接服务的地址
# 参数2 链接服务的参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desc)

time.sleep(3)
# 通过id进行定位
# id 是 resource-id属性 resource-id有可能重复，appium-desktop如果提供id定位方式代表没重复
# element = driver.find_element_by_id('com.tencent.mobileqq:id/btn_login')
# element = driver.find_element_by_id('btn_login')
# element.click()

# 通过class定位 属于重复属性 如果重复可以通过复数取角标方式定位
# element = driver.find_element_by_class_name('android.widget.Button')
# print(element)
# elements = driver.find_elements_by_class_name('android.widget.Button')[1]
# elements.click()

# 通过xpath 和web的相同 选择唯一属性定位
# //input
# //android.widget.Button[]
# element = driver.find_element_by_xpath("//android.widget.Button[@text='登 录']")
# element.click()


# accessibility_id 对应 content-desc属性 如果有这个属性 果断用
# element = driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
# element.send_keys('11111111')


# android 特有的定位方式
# element = driver.find_element_by_android_uiautomator('new UiSelector().text("登 录")')
# element.click()

