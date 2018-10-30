import logging

# 01初始化一个对象
logger = logging.getLogger()

# 02用来存放倒文件-FileHandler
# 02用来显示到控制台-StreamHandler
fh = logging.FileHandler('3.42-filehandle.log')
sh= logging.StreamHandler()

# 03设置错误等级
fh.setLevel(logging.DEBUG)
sh.setLevel(logging.WARNING)

# 04设置Formatter格式
log_format = logging.Formatter('-----\n出错文件名：%(filename)s\n时间：%(asctime)s'
                               '\n错误等级：%(levelname)s\n错误信息：%(message)s')

fh.setFormatter(log_format)     # 使用格式log_format
sh.setFormatter(log_format)     # 使用格式log_format

# 05 把handler 添加倒logeer对象中
logger.addHandler(fh)
logger.addHandler(sh)

# 抛出错误,生成一个filenmae日志文件
try:
    # 打开一个不存在的文件
    with open('notexist.txt') as f:
        pass
except Exception as e:
    logging.error(e)