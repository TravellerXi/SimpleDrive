#!/usr/bin/env python3
# coding:utf-8

def login(username,password):
    from methods.md5 import md5
    from methods.ErrorCode import UserNameError,PasswdError
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.CheckUsername(username=username) > 1:
        if Sql.CheckPassword(username, password) > 1:
            md5hash = md5(password)
            return md5hash
        else:
            return PasswdError
    else:
        return UserNameError

