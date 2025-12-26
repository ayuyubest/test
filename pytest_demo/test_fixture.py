import pytest

# fixture 是一个固定基线 在该基线上测试可以可靠重复的执行 区别于 setup teardown：
# 有独立命名 通过声明他们从测试函数 模块 类 或者整个项目来激活
# 按模块化的方式实现 每个fixture可以互相调用
# 从简单的单元扩展到复杂的功能测试
# 用于在测试前后的初始化设置 如准备测试数据 连接数据库 打开浏览器等操作
# 方式 @pytest.fixture() 用例调用fixture的返回值 直接就是把fixture 的函数名称当成变量名称
# fixture(scope='function',parames=None,autouse=False,ids=None,name=None)

# @pytest.fixture()
# def test1():
#     a = 'su'
#     print('test1方法传出a')
#     return a
#
# @pytest.fixture()
# def test2():
#     b = '男'
#     print('test2方法传出b')
#     return b
#
# class TestFixture:
#     def test_name(self, test1):
#         name = 'su'
#         print('找到name')
#         assert test1 == name
#
#     def test_sex(self, test2):
#         sex = '男'
#         print('找到sex')
#         assert test2 == sex


# python -m pytest pytest_demo/test_fixture.py -v -s
#===============================class 级别会话
# @pytest.fixture(scope='class')
# def test1():
#     b = '男'
#     print('传出%s,则只在class里面所有用例开始前执行一次'%b)
#     return b
# class TestCase:
#     def test_name(self, test1):
#         name = 'su'
#         print('找到name')
#         assert test1 == name
#
#     def test_sex(self, test1):
#         sex = '男'
#         print('找到sex')
#         assert test1 == sex
# 为session级别是可以跨.py 模块调用的 当有多个py文件的用例时 多个用例只需要调用一次，并且写到conftest.py 文件里
# =====
# fixture自动使用autouse= Ture
# ====================
# fixture 嵌套使用
order = []
# @pytest.fixture()
# def f1(f3):
#     order.append("f1")   #这里f3 传到f1 中
# @pytest.fixture()
# def f3():
#     order.append("f3")
# def test_1(f1): #参数为f1 调用f1 时候会先执行f1的参数f3
#     print(order)
#     assert order == ["f3","f1"]
# =======================
# fixture 参数化
# @pytest.fixture(params=['男','女'])  #将一个list 给params参数
# def fix(request):
#     return request.param #request.param 会依次将params里面的值返回去
# def test_9(fix):
#     print(fix)
# 如果有多个参数
li = [{'name':'ayuyu','age':'18'},{'name':'qwe','age':'23'}]
@pytest.fixture(params=li)
def fix(request):
    return request.param
def test_9(fix):
    print(fix['name'])
    print(fix['age'])
# =============
# fixture 做后置处理 通过yield关键字来实现