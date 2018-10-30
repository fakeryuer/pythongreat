import redis

# 本地win10
# r = redis.Redis(host='localhost',
#                 port=6379,
#                 db=1,
#                 decode_responses=True)  # decode_responses表示不是byte类型，为字符串类型

# 虚拟机
r = redis.Redis(host='192.168.198.128',port=6379, db=1, decode_responses=True)
print(r)


r.set('age', '188888')
a = r.get('age')
print(a)
print(type(a))