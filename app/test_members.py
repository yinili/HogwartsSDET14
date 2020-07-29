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

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class TestMembers:
    with open("datas/datas.yml") as f:
        testdatas = yaml.safe_load(f)

    with open("datas/deldatas.yml") as f:
        deldatas = yaml.safe_load(f)

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
    @pytest.mark.parametrize('name, gender, phone', testdatas)
    def test_addmembers(self, name, gender, phone):
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
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(name)

        # 步骤5 选择性别
        self.driver.find_element(MobileBy.ID, "e3m").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # 步骤6：输入手机号或者邮箱
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)

        # 步骤7：点击"保存"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 步骤8：验证toast提示"添加成功"
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" in result

    # 删除成员功能
    @pytest.mark.parametrize('name', deldatas)
    def test_delmembers(self, name):
        # 步骤1：点击"通讯录"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 步骤2：点击搜索
        self.driver.find_element(MobileBy.ID, "h9z").click()
        # 步骤3：搜索要删除的成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)

        elelist = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")

        if len(elelist) < 2:
            print('没有这个联系人')
            return
        elelist[1].click()

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
        time.sleep(5)

        # 步骤7：验证删除成功
        elelist_after = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")
        assert len(elelist) - len(elelist_after) == 1

    def teardown(self):
        self.driver.quit()
