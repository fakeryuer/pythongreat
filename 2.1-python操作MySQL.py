import pymysql

# 虚拟机连接
con = pymysql.connect(
    host = '192.168.198.128',
    port = 3306,
    user = 'yuhaoyu',
    password = 'yuer',
    db = 'hmqq',
    charset = 'utf8'
)
print(con)


cursor = con.cursor()
cursor.execute('SELECT 来源名称 FROM `飞鸟_直通车` limit 100;')        #执行sql
# one = cursor.fetchone()              #取出一条数据
all = cursor.fetchall()				 #取出所有数据
# print(one)
for i in all:
    print(i)

