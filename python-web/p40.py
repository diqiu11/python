#!/usr/bin/env python
# coding=utf-8
#json

import json
d = dict(name='bod',age=20)
print(json.dumps(d))

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
                'name':std.name,
                'age':std.age,
                'score':std.score
                }
    def dict2student(d):
        return Student(d['name'],d['age'],d['score'])

s1 = Student('diqiu',20,80)
json_str = '{"name":diqiu,"age":20,"score":80}'
print(json.dumps(s1,default=student2dict))
print(json.loads(json_str,object_hook=dict2student))
