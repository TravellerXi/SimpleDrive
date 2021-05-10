#!/usr/bin/env python3
# coding:utf-8
# pymysql ==0.9.3
import pymysql
import os


# TODO 修改return值，目前return值乱七八糟的。

class SqlMethod:
    def __init__(self):
        import configparser, sys
        if sys.path[0] == '':
            CurrentDir = os.getcwd()
        else:
            CurrentDir = sys.path[0]
        AbsolutePath = CurrentDir + '/Configure.ini'
        config = configparser.ConfigParser()
        config.read(AbsolutePath, encoding='utf-8')
        self.sqlservername = config.get('MySql', 'servername')
        self.sqluser = config.get('MySql', 'user')
        self.sqlpasswd = config.get('MySql', 'passwd')
        self.sqldatabase = config.get('MySql', 'database')

    def CheckUsername(self, username: str):
        """
        :param username: 用户输入的用户名
        :return:
        """
        db = pymysql.connect(self.sqlservername, self.sqluser, self.sqlpasswd, self.sqldatabase)
        check = db.cursor()
        usernameSQL = 'select username from ' + self.sqldatabase + '.user where username=' + "'" + username + "'"
        check.execute(usernameSQL)
        if (check.fetchone()) is None:
            db.close()
            return 0
        else:
            check.execute(usernameSQL)
            result = tuple(check.fetchone())
            result = ''.join(result)
            if username == result:
                db.close()
                return 2
            else:
                db.close()
                return 0

    def CheckPassword(self, username, password):
        """
        :param username: 用户名
        :param password: 密码
        :return:
        """
        db = pymysql.connect(self.sqlservername, self.sqluser, self.sqlpasswd, self.sqldatabase)
        check = db.cursor()
        passwordSQL = 'select passwd from ' + self.sqldatabase + '.user where username=' + "'" + username + "'"
        check.execute(passwordSQL)
        if check.fetchone() is None:
            db.close()
            return 0
        else:
            check.execute(passwordSQL)
            result = tuple(check.fetchone())
            result = ''.join(result)
            if password == result:
                db.close()
                return 2
            else:
                db.close()
                return 0

    def Checkmd5(self, md5, username):
        db = pymysql.connect(self.sqlservername, self.sqluser, self.sqlpasswd, self.sqldatabase)
        check = db.cursor()
        try:
            usernameSQL = 'select md5 from ' + self.sqldatabase + '.user where username=' + "'" + username + "'"
        except:
            return 0
        check.execute(usernameSQL)
        try:
            if (check.fetchone()) is None:
                db.close()
                return 0
            else:
                check.execute(usernameSQL)
                result = tuple(check.fetchone())
                result = ''.join(result)
                if md5 == result:
                    db.close()
                    return 2
                else:
                    db.close()
                    return 0
        except:
            return 0

    def Checkisadmin(self, username):
        db = pymysql.connect(self.sqlservername, self.sqluser, self.sqlpasswd, self.sqldatabase)
        check = db.cursor()
        usernameSQL = 'select isadmin from ' + self.sqldatabase + '.user where username=' + "'" + username + "'"
        check.execute(usernameSQL)
        if (check.fetchone()) is None:
            db.close()
            return 0
        else:
            check.execute(usernameSQL)
            result = tuple(check.fetchone())
            result = ''.join(result)
            if result == 'yes':
                db.close()
                return 2
            else:
                db.close()
                return 0
