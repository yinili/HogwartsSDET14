from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    contactlist = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        self.find_and_click(self.contactlist)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass
