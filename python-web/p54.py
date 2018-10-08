#!/usr/bin/env python
# coding=utf-8
#hashlib
import hashlib
def hash_t(passw):
    md5 = hashlib.md5()
    md5.update(passw.encode('utf-8'))
    print(md5.hexdigest())

hash1 = hash_t('wskg')
