#!/usr/bin/env python
# coding=utf-8
#hmac
import hmac

def hmac_t():
    key = b'sec'
    password = b'123456'
    h = hmac.new(key, password, digestmod='MD5')
    print(h.hexdigest())


b = hmac_t()
