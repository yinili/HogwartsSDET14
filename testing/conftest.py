import pytest
from pythoncode.calc import Calculator


@pytest.fixture(autouse=True)
def slogan():
    print("计算开始")
    yield
    print("计算结束")
