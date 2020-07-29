import pytest
import yaml

from app.page.app import App

# 读取添加成员测试数据
with open('../datas/deldatas.yml') as f:
    del_datas = yaml.safe_load(f)


class TestDelMem:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)

    @pytest.mark.parametrize('name', del_datas)
    def test_delmem(self, name):
        mypage = self.main.goto_contactlist().searchcontact(). \
            searchmem(name).personinfopage().infolistpage().delmem(name)

        result = mypage.verify_del()
        assert result == 1
