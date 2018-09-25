#!/usr/bin/env python
# coding=utf-8
import os
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'abc' for n in 'xyz'])
print([d for d in os.listdir('.')])
L = ['Hello', 'World','IBM','Apple']
print([s.lower() for s in L])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)==True]
print(L2)
