from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.test_wework_login.login import Login
from web.test_wework_login.register import Register


class Index:
    """
    首页po
    """

    def __init__(self):
        # options = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启
        #   options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """点击立即注册
           进入到注册的PO
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        """

        点击企业登录
        进入到企业登录的po
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn")
        return Login(self.driver)
