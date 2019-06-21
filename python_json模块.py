#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import json

print(json.__all__)

# 将python对象转换为json字符串
s = json.dumps(["gzy",{'favorite':('paint','music','coding',25)}])
print(s)

# 将python字符串转为json
s1 = json.dumps('ysilhouette')
print(s1)

# 将python dict对象转为json
s2 = json.dumps({"a":0,"b":1,"c":2},sort_keys=True)
print(s2)

# 将python 列表转为json
# 并指定json分割符，逗号。冒号之后没有空格
s3 = json.dumps([1,2,3,{'x':5,'y':7}],separators=(',',':'))
print(s3)

# 指定indent为4,意味转换json字符串有缩进
s4 = json.dumps({'python':5,'ios':4},sort_keys=True,indent=4)
print(s4)

# 使用JSONEncoder的encode方法 将python转为json
s5 = json.JSONEncoder().encode({"name":("gzy","ysilhouette")})
print(s5)

f = open('python_json_learn.json','w')
# 使用dump()函数，将转换得到的json字符串输出到文件
json.dump(['gzy',{'python':5,'ios':4}],f)