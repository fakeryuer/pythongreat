import json

# 定义一个Python形式的数据
data = {
    'name':'泓清泉',
    'age':'23',
    'interest':{1:'game1',2:'game2'}
}

# 01将python数据转为为json格式字符串
j1 = json.dumps(data, ensure_ascii=False)           # 默认中文使用ASCII码-ensure_ascii=True
j2 = json.dumps(data,indent=2, sort_keys=True)          # indent=n:对齐n个字符，格式化；sort_keys排序
# print(j1)
# print(j2)
print(type(j1))

# 02将json数据转为python数据
p1 = json.loads(j1)
key = p1['interest']
print(p1)
print(type(p1))
print('按key取值',key)

# 03转换为json，并保存倒文件
fp = open('3.1.1-json文件.json','w+')     # 当前目录生成一个.json文件
json.dump(data,fp,indent=2)
fp.close()

# 04读取json文件，转为python数据类型
fp2 = open('3.1.1-json文件.json','r')
p2 = json.load(fp2)
print('读取json文件',p2)
fp2.close()