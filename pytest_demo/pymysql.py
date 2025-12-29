# pymysql 是用来专门操作数据库的
import pymysql
conn  = pymysql.connect("localhost",user="root",password="123456",charset='utf8')
conn = select_db("pythondb")
cur = conn.cursor() #获取游标 操作数据库
cur.execute("create table ...") #执行创建表语句

res = cur.fetchall()  #显示全部查出内容
cur.close() #关闭游标
conn.commit()# 提交数据
conn.close() #关闭数据库
