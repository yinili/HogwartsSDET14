"""
编写添加联系人测试用例
编写删除联系人测试用例

编码代码的时候注意点：

1、添加联系人页面动态的查找【添加成员】按钮
学习滚动查找页面元素
2、定位方式
学习多种定位方式的灵活运用
3、断言
验证页面的正确性
4、加分项：
使用 setup_class,teardown_class 初始化，使用setup,teardown 完成测试用例之间的切换
使用有规律的联系人名称，例如【霍格沃兹_1】，方便删除联系人
实现allure 测试报告生成
"""
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class TestMembers:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0
        caps['automationName'] = 'uiautomator2'  # 获取toast必备

        # 与server 建立连接,初始化一个driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    # 添加成员功能
    def test_addmembers(self):
        name = "霍格沃兹_1"
        # 步骤1：点击"通讯录"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 步骤2：点击"添加成员"
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("添加成员").instance(0));').click()
        # 步骤3：点击"手动输入添加"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 步骤4：输入"姓名"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys("霍格沃兹_1")
        # 步骤5：选择性别
        self.driver.find_element(MobileBy.ID, "e3m").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 步骤6：输入手机号或者邮箱
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("13000000001")
        # 步骤7：点击"保存"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 步骤8：验证toast提示"添加成功"
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" in result

    # 删除成员功能
    def test_delmembers(self):
        # 步骤1：点击"通讯录"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 步骤2：点击要删除的成员姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@text='霍格沃兹_1']").click()
        # 步骤3：点击右上角"..."
        self.driver.find_element(MobileBy.ID, "h9p").click()
        # 步骤4：点击"编辑成员"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 步骤5：滑动查找"删除成员"后点击
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("删除成员").instance(0));').click()
        # 步骤6：点击toast中的确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        # 步骤7：验证删除成功
        result = self.driver.find_element(MobileBy.ID, "b2z").text
        assert "霍格沃兹_1" not in result

    def teardown(self):
        self.driver.quit()
