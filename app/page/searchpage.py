from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.PersonInfoPage import PersonInfoPage

"""
搜索页面
"""


class SearchPage(BasePage):
    search_ele1 = (MobileBy.XPATH, "//*[@text='搜索']")
    search_ele2 = (MobileBy.ID, "h9p")

    def searchmem(self, name):
        # 搜索成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        self.find_and_sendkeys(self.search_ele1, name)
        sleep(3)
        # 获取联系人列表
        global elelist
        elelist = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")
        # 判断搜索出来的列表长度
        if len(elelist) < 2:
            print('没有这个联系人')
            return

        # 如果存在联系人，点击第一个
        elelist[1].click()
        # 进入个人信息概览页面
        return PersonInfoPage(self.driver)

    def verify_del(self, name):
        elelist_after = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")
        result = len(elelist) - len(elelist_after)
        return result
