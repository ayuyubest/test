import requests
from pandas.io.sas.sas_constants import header_size_length
#
# response  = requests.get("https://www.baidu.com/")
# print(response.text)
# # 带请求参数 的get请求  先定义一个 字典 在调用get请求时将字典赋值给params参数
# data={
#     'name':'ayuyu',age=22
# }
# response  = requests.get("https://www.baidu.com/",params=data)
# print(response.text)
# # 3 解析json
# # json用来保存一些键值对组成的数据，用于数据交换 比如前端调用接口 后端返回一串json数据渲染到页面
# response  = requests.get("https://www.baidu.com/")
# print(type(response.json()))
# 4 获取二进制数据 一般用于下载图片视频等
# response  = requests.get("https://www.baidu.com/")
# # print(type(response.content)
# with open("favicon.ico","wb") as f: # 处理二进制数据的保存
#     f.write(response.content)
#     f.close()
# 5 添加 headers
# headers = {}
# 6 post 请求
# headers = {}
# data = {}
# response = requests.post("https://www.baidu.com/",data=data,headers=headers) #有参数用data 不用parames
# # 7 response 属性
# # 8状态码判断
# 9-1 requests 高级操作 上传文件
# files = {"file":open("favion.ico",''rb)}
# response = requests.post("https://www.baidu.com/",files=files)
# 9-2 获取cookie
# cookie是存储用户在特定网站上个的密码和id，也是存储起始页的首选项 每次登陆该网站时 浏览器将检查是否有cookie 有则浏览器将此cookie一起发给服务器
# 会话维持用来模拟登陆
# session类用来实现客户端和服务端的会话维持
s = requests.session()
s.get()
response = s.get()
print(response.text)
# 超时设置
# 代理设置
# 认证设置