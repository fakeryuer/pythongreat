import logging

'''
%(fliename)s 文件名
%(levelname)s 文本形式的日志级别
%(message)s 用户输出的消息
%(asctime)s 字符串形式的当前时间
'''
# 定义格式
log_format = '%(filename)s--%(asctime)s--%(levelname)s--%(message)s'
# 配置               filename 路径、文件名     level 错误等级    format 记录格式
logging.basicConfig(filename='3.41-my.log', level=logging.ERROR, format=log_format)


# 抛出错误，如果未配置且错误等级过低，不记录，默认记录warning以上等级
logging.log(logging.ERROR, 'fakeryu')

# 如何捕捉异常错误
try:
    # 打开一个不存在的文件
    with open('notexist.txt') as f:
        pass
except Exception as e:
    logging.error(e)

print('程序继续运行')