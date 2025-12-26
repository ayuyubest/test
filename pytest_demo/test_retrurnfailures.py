import pytest

# 用法1：命令行输入 pytest --reruns n
# 用法2:修改配置文件 addopts = -s --html=report/report.html --reruns 3
# 失败重跑意义：重跑这个case 直到跑完n次或者这个case返回了Ture就可以停停止
#===========================
# 跳过测试函数  condition 必填，跳过的条件； reason 非必填
# @pytest.mark.skipif(condition,reason=None)

class TestRetryAndSkip:
    @pytest.mark.skipif(True, reason='演示跳过测试')
    def test_success3(self):
        print("success4")


# 运行 python -m pytest pytest_demo/test_retrurnfailures.py -s -v