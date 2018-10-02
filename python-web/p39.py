#!/usr/bin/env python
# coding=utf-8
import pickle
d = dict(name='bod',age=20)
print(pickle.dumps(d))
pickle.dumps(d)
f = open('test.txt','wb')
pickle.dump(d,f)
f.close

