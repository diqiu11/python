#!/usr/bin/env python
# coding=utf-8
#枚举
from enum import Enum, unique
@unique
class Gender(Enum):
   # gender = Enum('gender',('male','female'))
   # for name,gen in gender.__members__.item():
       # print(name, '=',gen,'is',gen.value )
    male = 0
    female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name

        if type(gender) == Gender:
            self.gender = gender
        else:
            raise TypeError('404')

bart = Student('Bart', Gender.male)
if bart.gender == Gender.male:
    print('测试通过!')
else:
    print('测试失败!')


