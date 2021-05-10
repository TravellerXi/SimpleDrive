#!/usr/bin/python
# coding:utf-8
def md5(password):
    import hashlib
    password=password.encode(encoding='utf-8')
    hashedPassword=hashlib.md5()
    hashedPassword.update(password)
    return (hashedPassword.hexdigest())
