# from app.page.addmemberpage import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage


class ContactAddPage(BasePage):
    findname = (MobileBy.XPATH, "//*[@text='必填']")
    findgender = (MobileBy.ID, "e3m")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    findphone = (MobileBy.XPATH, "//*[@text='手机号']")
    findsave = (MobileBy.XPATH, "//*[@text='保存']")

    def set_name(self, name):
        self.find_and_sendkeys(self.findname, name)
        return self

    # 选择性别
    def set_gender(self, gender):
        # self.driver.find_element(MobileBy.ID, "e3m").click()
        self.find_and_click(self.findgender)
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.male_ele)
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self.female_ele)
        return self

    # 编辑手机号
    def set_phone(self, phone):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        self.find_and_sendkeys(self.findphone, phone)
        return self

    def click_save(self):
        from app.page.addmemberpage import AddMemberPage
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.find_and_click(self.findsave)
        return AddMemberPage(self.driver)
