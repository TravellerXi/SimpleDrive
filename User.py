#!/usr/bin/env python3
# coding:utf-8

class User:
    def login(self,username,password):
        import md5
        from ErrorCode import UserNameError,PasswdError
        from Sql import Sql
        if Sql.CheckUsername(username) > 1:
            if Sql.CheckPassword(username, password) > 1:
                md5hash = md5(password)
                return md5hash
            else:
                return PasswdError
        else:
            return UserNameError

