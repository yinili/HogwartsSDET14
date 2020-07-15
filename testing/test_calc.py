"""
SDET-14课后作业一

1、补全计算器（加减乘除）的测试用例

2、使用数据驱动完成测试用例的自动生成

3、conftest.py中创建fixture 完成setup和teardown

4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

from pythoncode.calc import Calculator
import pytest


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()

    """ 加法 """

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 2),
        (0.1, 0.1, 0.2),
        (-1, 1, 0),
        (-1, -1, -2),
        (1, 0.1, 1.1)
    ])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)


    """ 除法 """

    @pytest.mark.dependency(depends=['test_multiple'])
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 1),
        (0.1, 0.1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (1, 0.1, 10),
        (0, 1, 0),
        (1, 0, 0),
        (1, 2, 0.5)
    ])
    def test_div(self, a, b, result):
        try:
            assert result == self.cal.div(a, b)
        except ZeroDivisionError as e:
            return "除数不能为0！"

    """ 减法 """

    @pytest.mark.dependency(depends=['test_add'])
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 0),
        (0.1, 0.1, 0),
        (-1, 1, -2),
        (-1, -1, 0),
        (1, -1, 2),
        (-1, 1, -2)
    ])
    def test_minus(self, a, b, result):
        assert result == self.cal.minus(a, b)

    """ 乘法 """

    @pytest.mark.multiple
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 1),
        (0.1, 0.1, 0.01),
        (-1, 1, -1),
        (-1, -1, 1),
        (1, 0.1, 0.1),
        (0, 1, 0),
        (0, 0.1, 0)
    ])
    def test_multiple(self, a, b, result):
        assert result == self.cal.multiple(a, b)
