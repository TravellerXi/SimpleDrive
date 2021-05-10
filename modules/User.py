#!/usr/bin/env python3
# coding:utf-8


class User:
    def login(self,username,password):
        from methods.md5 import md5
        from methods.ErrorCode import UserNameError,PasswdError
        from Sql import SqlMethod as Sql
        if Sql.CheckUsername(username) > 1:
            if Sql.CheckPassword(username, password) > 1:
                md5hash = md5(password)
                return md5hash
            else:
                return PasswdError
        else:
            return UserNameError

