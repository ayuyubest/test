# 函数数据参数化
# parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
# argnames 参数名 argnames 参数值 类型必须为list [v1,v2,v3]  多个时 (v1,v2),(b1,b2)
import pytest

# 方法
# @pytest.Mark.parametrize(argnames,argvalues)
# @pytest.Mark.parametrize('name',['v1','v2']) #1个参数时
# @pytest.Mark.parametrize(('name1','name2'),[('v1','v2'),('v3','v4')]) #多个参数时
def setup(self):
    server = r''
    desired_capabilities = {
        'name':'1',
        'key':'123456'
    }
    self.driver = webdriver.Remote(server,desired_capabilities)
    # 参数化方法 参数名和下面的参数名一致
    @pytest.mark.parametrize('name',['name1','name2','name3'])
    def test_search(self,name)  #参数名和下面的参数名一致
    # 如果是多个参数
    @pytest.mark.parametrize(('name','value'), [('name1','123'), ('name2','456')])
    def test_search(self, name,value)  # 参数名和下面的参数名一致

