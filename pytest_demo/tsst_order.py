import pytest
class TestLogin:
    @pytest.mark.run(order=0)
    def test_success1(self):
        print("test success1")
    @pytest.mark.run(order=2)
    def test_fail(self):
        print("test fail")
    @pytest.mark.run(order=1)
    def test_success2(self):
        print("test success2")

# 运行 python -m pytest pytest_demo/tsst_order.py -s -v
