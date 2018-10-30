import hashlib

# 简单密码需要加盐，防止暴力破解
pw = '123456'.encode()+'abcdefg'.encode()       # abcdefg 盐

# md5加密
h1 = hashlib.md5(pw)    # 只能对byte类型转换

'''
常用加密方法：
md5
sha1
sha224\256\384\512
'''

print(h1)
# 查看加密后的密码
print('加密后的：',h1.hexdigest())   # str形式
print('加密后的：',h1.digest())  # 二进制形式

# 上述加密对密码都不太合适
    #通常的加盐方式
pw2 = '123456'.encode()
salt = 'asdasda'.encode()

h2 = hashlib.md5()  # 只创建对象，不加参数
h2.update(pw2)      # update会累积更新
print(h2.hexdigest())
h2.update(salt)     # pw+salt1加密
print('salt一次',h2.hexdigest())
h2.update(salt)     # pw+salt2加密
print('salt二次',h2.hexdigest())

# 安全的加密方式：
    # pbkdf2_hmac(加密方式，加密对象，盐，加盐循环次数，决定长度）
h3 = hashlib.pbkdf2_hmac('md5', pw2, salt, 100000)  # 通常对密码加密，直接返回加密后的值
print('安全的加密方式',h3)