#!/usr/bin/env python
# coding=utf-8
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        try:
            if self.score >= 60 and self.score <= 79:
                return 'B'
            if self.score >= 80 and self.score <= 100:
                return 'A'
            if self.score >=0 and self.score <= 59:
                return 'C'
            if self.score >=101 and self.score < 0:
                raise ValueError
        except:
            raise ValueError


        

