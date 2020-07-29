"""
通讯录列表页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.addmemberpage import AddMemberPage
from app.page.searchpage import SearchPage

search_ele = (MobileBy.ID, "h9z")


class ContactListPage(BasePage):

    # 进入添加成员页面
    def addcontact(self):
        # self.driver.find_element(
        #    MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
        #                                 '(new UiSelector().'
        #                                 'scrollable(true).'
        #                                 'instance(0)).'
        #                                 'scrollIntoView('
        #                                 'new UiSelector().'
        #                                 'text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return AddMemberPage(self.driver)

    # 进入搜索成员页面
    search_ele = (MobileBy.ID, "com.tencent.wework:id/gq_")

    def searchcontact(self):
        # 点击搜索框
        # self.driver.find_element(MobileBy.ID, "h9z").click()
        self.find_and_click(self.search_ele)
        return SearchPage(self.driver)
