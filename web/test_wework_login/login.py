from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from web.test_wework_login.register import Register


class Login:
    """
    登录页面po
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """点击登录注册
           进入到注册的PO
        """
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self.driver)
