from datetime import datetime


# datetime.date( year, month, day )
# datetime.time( hour, minute, second, microsecond )
# datetime.datetime( year, month, day,hour, minute, second, microsecond )
# datetime.timedelta( days=0, seconds=0, microseconds=0 milliseconds=0,minutes=0, hours=0, weeks=0 )

# 获取系统时间
now = datetime.now()
# 获取时间戳
sp = now.timestamp()
# 时间错戳化为时间
sj = datetime.fromtimestamp(sp)

print(now)
print(sp)
print(sj)


# 字符串转换为时间对象
strtime = '1995-8-15'
day = datetime.strptime(strtime, '%Y-%m-%d')        # Y为四位，y为两位
print(day)
# 时间日期转字符串
a = datetime(2099,9,9,13,59,59)
stime = datetime.strftime(a, '%y-%m-%d %H:%M:%S')
print(stime)


# 时间计算
import datetime
tomorrow = datetime.timedelta(days=100) + datetime.datetime.now()
print(tomorrow)