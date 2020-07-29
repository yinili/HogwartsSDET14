from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.InfoListPage import InfoListPage

"""
个人信息概览页
"""


class PersonInfoPage(BasePage):
    click_ele = (MobileBy.ID, "h9p")

    def personinfopage(self):
        # 点击右上角，进入个人信息详情页
        # self.driver.find_element(MobileBy.ID, "h9p").click()
        self.find_and_click(self.click_ele)

        return InfoListPage(self.driver)
