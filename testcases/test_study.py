# _*_ coding:utf-8 _*_
'''
关于pytest的前置处理、后置处理的说明
    1、函数在类外，方法在类内
    2、setup_module/teardown_module为函数的前/后置处理，所有类外用例函数均会执行
    3、setup_method/teardown_method为方法的前/后置处理，需要写在对应的类内，类内的每个方法执行都会执行一次
    4、setup_class/teardown_class为类的前/后置处理，需要写在对应的内内，该类执行是在所有方法执行的前后只执行一次
    5、setup_module/town_module为文件的前/后置处理，需要写在对应的文件内，该文件的所有函数、方法执行前后只执行一次
关于paramatrize进行参数化
    @pytest.mark.paramatrize()
        单参数化：@pytest.mark.paramatrize('变量名称',取值对象,ids="命名")
        多参数化：@pytest.mark.paramatrize('变量名称1,变量名称2',[多个参数对的列表/元组],ids=["命名1","命名2"])
            多参数时各项的数量必须匹配
        笛卡尔积方法：多组单参数的组合形式
关于特定测试用例的标记以及执行：
    使用mark进行标记，标记方式为在同一类测试用例方法进行装饰器标记：@pytest.mark.名称  名称要求为英文，且该名称需要在pytest.ini文件的markers记录
    特定测试用例的执行为 -m 名称
跳过及预期失败
    1、skip:始终跳过该测试用例
    2、skipif:遇到特定情况跳过该测试用例
    3、xfail:遇到特定情况产生一个期望的输出

    1）调试时不想运行这个用例
    2）标记无法在某些平台商运行的测试功能
    3）在某些版本执行，其他版本跳过

    skip用法：
        1、@pytest.mark.skip(reason="")
        2、在代码中需要执行的位置：pytest.skip(reason="")
        上述两种方法均可将需要跳过的测试用例进行跳过，并输出跳过原因
    skipif用法：
        @pytest.mark.skipif(跳过条件,reason="")
        当满足“跳过条件”时标记的测试用例跳过不执行，并输出reason信息
    xfail用法：
        方式一：@pytest.mark.xfail
        被@pytest.mark.xfail标记的测试用例，会正常执行，当用例通过输出为xpass，否则输出xfail
            主要应用于待修复bug用例，作为参考
        方式二：也可以将xfail使用到代码中，但使用后后边的代码将不被执行
        方式一相对方式二的优点在于用例会完整执行，其输出结果可用于同步监控代码是否已修复完成
测试用例的选择运行：
    执行包下所有的用例：pytest/py.test [包名]
    执行单独一个pytest模块：pytest 文件名.py
    执行某个模块的特定的某个类：pytest 文件名.py::类名
    执行某个模块下的某个类的某个方法用例：pytest 文件名.py::类名::方法名
--lf(--last-failed)只重新运行故障用例
--ff(--failed-first)先运行故障用例然后再运行其他用例

常用pytest命令
    --help
    -x  用例一旦失败（fail/error），就立刻停止执行，常用于冒烟测试
    --maxfail=num   用例达到
    -m  标记用例
    -k  执行包含某个关键字的测试用例
    -v  打印详细日志
    -s  打印输出日志（一般-vs一起使用）
    --collect-only   只收集不运行（测试平台，pytest自动导入功能）
python解释器执行pytest用例
    方式一：
        if __name__ =="__main__":
            pytest.main(['-vs'])    #执行当前目录下的所有测试用例
            pytest.main(['test_file.py','-vs'])     #执行指定文件模块下的所有测试用例
            pytest.main(['test_file.py::TestCase','-vs'])   #执行指定模块下指定类下的测试用例
            pytest.main(['test_file.py::TestCase','-vs','-m','标记名称'])   #执行指定模块下指定类下指定标记名称的测试用例
        然后直接终端运行“if __name__ =="__main__"”所在的文件即可：python file.py
    方式二：
        python -m pytest -vs test_file.py
            在已有pytest解释器命令行的基础上添加了“python -m”，主要用于持续集成
在实际执行中使用python解释器而不直接使用pytest解释器的原因：
    1、直接使用python解释器可以同时调用其他python文件
    2、当用例编写包含了多种版本python时比较容易指定python版本

pytest异常处理
    1、try...except...
    2、pytest.raise()


'''

import pytest,requests
from python_study.pytest_demo.file_read import get_excel
from python_study.pytest_demo.common import get_log
from datetime import datetime

def setup_module():
    print("文件级别的初始化文件")
def teardown_module():
    print("文件级别的后置处理器")

def setup_function():
    print("函数级别的前置处理")
def teardown_function():
    print("函数级别的后置处理")


def test_1():
    a = 1
    b = 2
    assert a < b,"实际结果与预期不符"

#单参数化示例
list_b = ["小明","小李","小曹"]
@pytest.mark.parametrize('name',list_b)
def test_2(name):
    b = ["小明","小李","小曹","小董"]
    assert name in b,"实际结果不在预期列表范围"

@pytest.mark.xfail(reason="这是个待修复bug")
def test_3():
    a = 3
    b = 4
    assert a == b
def test_4():
    pytest.xfail(reason="bug未修复")#后续代码不会被执行
    assert 3<4

@pytest.mark.skip(reason="这是skip的跳过")
def test_5():
    print("校验skip装饰器是否被执行")

@pytest.mark.skipif(AssertionError,reason="功能尚未实现")
def test_6():
    namelist = ["小明","小丽","小红"]
    assert "小花" in namelist



#pytest.raise()抛出异常，注（match信息要与抛出异常的信息匹配才可以通过，日常操作中一般match信息可以忽略不添加）
def test_raise():
    with pytest.raises((ZeroDivisionError,ValueError),match="抛出异常"):    #抛出两种异常中的任意一种就可以通过
        raise ZeroDivisionError("抛出异常")
#使用抛出异常并检查异常信息
def test_pytest_raise():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("Value error")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] =="Value error"




class TestMeeting:
    def setup_class(self):
        print("类级别的前置处理器")
    def teardown_class(self):
        print("类级别的后置处理器")

    def setup_method(self):
        print("方法级别的前置处理器")
    def teardown_method(self):
        print("方法级别的后置处理器")


#通过笛卡尔积参数化来进行会议id与密钥source参会的匹配校验

    list_id = [33977,33978]
    @pytest.mark.parametrize('id',list_id)
    def test_根据会议ID获取会议报名列表信息(self,id):
        url = "https://api-stress.ma.scrmtech.com/app-api/meetingSap/signUp"
        data = {
            "source": 225,
            "secret": "3bf5bda694a7d20485cfc01c4d7c01d0",
            "appid": "wxae4d2a32bee4a05b",
            "meeting_id":id,
            "active":"",
            "start_time":"",
            "end_time":"",
            "page_no":"",
            "page_size":""
        }
        res = requests.get(url, data)
        content = res.json()
        code = content['code']
        data  = content['data']
        print(data['total'])
        assert code == 0
        # 设置日志名称
        name = "case" + datetime.now().date().strftime('%Y%m%d') + ".log"
        logger = get_log.get_log(name)
        # 设置log输出信息内容
        logger.info('请求地址是{},请求参数是{},响应信息是{}'.format(url, data, res.json()))
        assert code == 0

    @pytest.mark.parametrize("source,appid,secret",get_excel())
    def test_会议行为记录(self,source,appid,secret):
        url = "https://api-stress.ma.scrmtech.com/app-api/meeting/standard/meeting/behaviorLog"
        data = {
            "source": source,
            "secret": secret,
            "appid": appid,
            "id":33977,
            "start_time": "",
            "end_time": "",
            "page_no": "",
            "page_size": ""
        }
        res = requests.post(url,data)
        content = res.json()
        code = content['code']
        # 设置日志名称
        name = "case" + datetime.now().date().strftime('%Y%m%d') + ".log"
        logger = get_log.get_log(name)
        #设置log输出信息内容
        logger.info('请求地址是{},请求参数是{},响应信息是{}'.format(url,data,res.json()))
        assert code == 0


