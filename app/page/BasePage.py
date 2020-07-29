"""
BasePage:用来存放一些基本的方法，比如初始化driver，find查找元素
"""
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    # 初始化方法，接收driver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_by_scroll(self, text):
        return self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector()'
                                          '.scrollable(true)'
                                          '.instance(0)'
                                          '.scrollIntoView(new UiSelector())'
            f'.text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
