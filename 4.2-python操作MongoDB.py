import pymongo

# 01建立连接
conn = pymongo.MongoClient(
    '192.168.198.128',27017
)
# print(conn)
# print(conn.database_names())      # 获得所有数据库名字
# 02指定数据库

db = conn['yu_mgdb']
# print(db.collection_names())     # 获得所有集合名字

# 03指定集合
collection = db['yu_table']

# 04插入数据
masge = {'name':'pycharm',
         'ag':'test'
         }
collection.insert(masge)

# 05查找数据
result = collection.find()

for i in result:
    print(result)

# 😂删除数据
# collection.delete_one({'name':'pychamr'})     # 删除一条