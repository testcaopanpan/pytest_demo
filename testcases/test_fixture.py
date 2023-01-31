# _*_ coding:utf-8 _*_
import pytest

@pytest.fixture()
def login():
    print("这是登录函数")             #相当于setup
    yield                           #yield前的代码时setup前置函数，后边的代码时teardown后置函数
    print("这是退出登录的函数")        #相当于teardown



def test_01(login):
    print("test_01用例")

def test_02():
    print("test_02用例")

def test_03():
    print("test_03用例")

