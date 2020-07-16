"""
课后作业1
1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例

课后作业2
控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
减法依赖加法， 除法依赖乘法

课后作业3
注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。

理解
测试数据的数据驱动
测试步骤的数据驱动
思考应用场景
"""

from pythoncode.calc import Calculator
import pytest
import yaml

with open("datas/test/data.yml") as f:
    testdatas = yaml.safe_load(f)
    # 加法测试数据
    addids = testdatas['add'].keys()
    adddatas = testdatas['add'].values()
    # 除法测试数据
    divids = testdatas['div'].keys()
    divdatas = testdatas['div'].values()
    # 减法测试数据
    minusids = testdatas['minus'].keys()
    minusdatas = testdatas['minus'].values()
    # 乘法测试数据
    multipleids = testdatas['multiple'].keys()
    multipledatas = testdatas['multiple'].values()


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()

    """ 加法 """

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', adddatas, ids=addids)
    def check_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    """ 除法 """

    @pytest.mark.div
    @pytest.mark.dependency(depends=['test_multiple'])
    @pytest.mark.parametrize('a, b, result', divdatas, ids=divids)
    def check_div(self, a, b, result):
        try:
            assert result == self.cal.div(a, b)
        except ZeroDivisionError as e:
            return "除数不能为0！"

    """ 减法 """

    @pytest.mark.minus
    @pytest.mark.dependency(depends=['test_add'])
    @pytest.mark.parametrize('a, b, result', minusdatas, ids=minusids)
    def check_minus(self, a, b, result):
        assert result == self.cal.minus(a, b)

    """ 乘法 """

    @pytest.mark.multiple
    @pytest.mark.parametrize('a, b, result', multipledatas, ids=multipleids)
    def check_multiple(self, a, b, result):
        assert result == self.cal.multiple(a, b)
