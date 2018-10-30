import base64

u = 'fakeryu'.encode()

# 编码
result_e = base64.b64encode(u)
# 解码
result_d = base64.b64encode(result_e)


# url编码|解码
url = 'www.baidu.com'
a = base64.urlsafe_b64encode(url)
base64.urlsafe_b64decode(a)