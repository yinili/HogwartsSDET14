# from app.page.contactaddpage import ContactAddPage

"""
添加成员页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage


class AddMemberPage(BasePage):
    contactadd = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_menual(self):
        from app.page.contactaddpage import ContactAddPage
        # 步骤3：点击"手动输入添加"
        self.find_and_click(self.contactadd)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        element = self.webdriver_wait(self.toast_ele)
        result = element.text
        return result
