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
    # "appActivity":".Settings",
    "appActivity":"com.tencent.mobileqq.activity.SplashActivity",
    "noReset":True

}
# 默认appiumserver的服务端口是4723
# 参数1 链接服务的地址
# 参数2 链接服务的参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desc)


# 滑动屏幕
# size = driver.get_window_size()
# height = size.get('height')
# width = size.get('width')
# y1 = height * 0.8
# x1 = width * 0.5
# y2 = height * 0.2
# x2 =width * 0.5
# driver.swipe(x1,y1,x2,y2)

# 操作app的api
# 判断某个app是否被安装  接收包名
# print(driver.is_app_installed('com.tencent.mobileqq'))
#
# # 卸载
# driver.remove_app('com.tencent.mobileqq')
#
# # 安装
# driver.install_app('/Users/houyafan/Desktop/mobileqq_android.apk')

# # 关闭初始化中的app
# driver.close_app()
#
# # 启动初始化app
# driver.launch_app()

# 打印当前activity
# print(driver.current_activity)
# 启动多个app
# driver.start_activity('com.tencent.mobileqq','com.tencent.mobileqq.activity.SplashActivity')

# 讲app 退到桌面 5秒后在启动
# driver.background_app(5)

# 调用就初始化
# driver.reset()