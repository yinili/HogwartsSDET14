from typing import List
import pytest
import yaml


@pytest.fixture(autouse=True)
def slogan():
    print("计算开始")
    yield
    print("计算结束")


# 控制测试用例顺序按照【加-减-乘-除】这个顺序执行
def pytest_collection_modifyitems(items: List["Item"]):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.run(order=1))
        if 'minus' in item.nodeid:
            item.add_marker(pytest.mark.run(order=2))
        if 'multiple' in item.nodeid:
            item.add_marker(pytest.mark.run(order=3))
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.run(order=4))


# 自定义命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your own run env')


# 解析命令行参数
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/env.yml'
    if myenv == 'dev':
        datapath = 'datas/dev/env.yml'

    # 读取文件路径
    with open(datapath) as f:
        datas = yaml.safe_load(f)
        return myenv, datas
