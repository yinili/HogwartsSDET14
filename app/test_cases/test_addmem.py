import pytest
import yaml

from app.page.app import App

# 读取添加成员测试数据
with open('../datas/adddatas.yml') as f:
    add_datas = yaml.safe_load(f)


class TestAddMem:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)

    @pytest.mark.parametrize('name, gender, phone', add_datas)
    def test_addmem(self, name, gender, phone):
        # name = "霍格name5"
        # gender = "男"
        # phone = "13000000005"
        mypage = self.main.goto_contactlist().addcontact().add_menual(). \
            set_name(name).set_gender(gender).set_phone(phone).click_save()
        text = mypage.get_toast()
        assert "添加成功" in text
        self.app.back()
