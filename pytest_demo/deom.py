import pytest

def test_success():
    print("test_success")
    assert True

def test_fail():
    print("test_fail")
    assert False

if __name__ == '__main__':
    # 定义一个列表 列表内容为测试文件名 也可以定义为元组 表示需要运行的文件为demo.py
    test_list = ['deom.py']
    # 用pytest 模块的main 方法， 参数为上面定义的列表/元组
    # pytest.main(test_list)
    pytest.main(['-s','demo.py'])

# 测试文件名以test_开头 或者_test结尾
# 测试方法必须test_开头
# 测试类名 以Test开头