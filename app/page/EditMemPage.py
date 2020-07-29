"""
编辑成员页面
"""
import time

from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage


class EditMemPage(BasePage):
    toast_ele = (MobileBy.XPATH, "//*[@text='确定']")

    def delmem(self):
        from app.page.searchpage import SearchPage
        # self.driver.find_element(
        #    MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
        #                                 '(new UiSelector().'
        #                                 'scrollable(true).'
        #                                 'instance(0)).'
        #                                 'scrollIntoView('
        #                                 'new UiSelector().'
        #                                 'text("删除成员").instance(0));').click()
        self.find_by_scroll("删除成员").click()

        # 步骤6：点击toast中的确定
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        self.find_and_click(self.toast_ele)
        time.sleep(5)
        return SearchPage(self.driver)
