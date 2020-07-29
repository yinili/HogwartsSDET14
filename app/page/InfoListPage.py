from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.EditMemPage import EditMemPage

"""
个人信息列表页面
"""


class InfoListPage(BasePage):
    list_ele = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def infolistpage(self):
        # 点击编辑成员，进入成员编辑页面
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.find_and_click(self.list_ele)
        return EditMemPage(self.driver)
