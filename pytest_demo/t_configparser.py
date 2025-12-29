# configparser 模块是读取配置文件模块
import configparser
# 创建一个解析器
config = configparser.ConfigParser()
# 读取config内容并解析
config.read('config.ini',encoding='utf-8')
# 使用get方法获取配置文件内容 返回内容是str类型
config.get('DATABASE','host')
