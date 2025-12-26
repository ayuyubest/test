# setup() 和 teardown() 是两个特殊的方法 setup() 是在每个测试用例执行前都会执行的方法 teardown（）是执行后都要执行的方法
# class TestLogin:
#     def setup_method(self):
#         print("setup")
#
#     def teardown_method(self):
#         print("teardown")
#
#     def test_success(self):
#         print("test success")
#
#     def test_fail(self):
#         print("test fail")
 # 运行 pytest -s test_setup.py
# =================================================================
 # setup_class teardown_class  每一个测试类执行前后都要执行的方法

class TestLogin:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")

    def setup_method(self):
        print("setup")

    def teardown_method(self):
        print("teardown")

    def test_success(self):
        print("test success")

    def test_fail(self):
        print("test fail")
# 运行 pytest -s test_setup.py
# setupclass 可以写连接手机的代码 teardown class 写退出driver的代码
