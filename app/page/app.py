"""
存放app应用常用的一些方法：比如启动APP，关闭APP等
"""
from appium import webdriver

from app.page.BasePage import BasePage
from app.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        """
        启动app
        :return:
        """
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["noReset"] = "true"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0
            caps['automationName'] = 'uiautomator2'  # 获取toast必备

            # 与server 建立连接,初始化一个driver
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(15)
        return self

    def restart(self):
        """
        重启app
        :return:
        """
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        关闭app
        :return:
        """
        self.driver.quit()

    def goto_main(self):
        """
        进入首页
        :return:
        """
        return MainPage(self.driver)
