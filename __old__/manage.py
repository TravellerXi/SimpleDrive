#!/usr/bin/python
# coding:utf-8

import pymysql
from managehtml import *
from md5 import *
import os

sqlservername='localhost'
sqluser='simpledrive'
sqlpasswd='simpledrive'
sqldatabase='simpledrive'

def manageUserandServer(username):
    isadmin=''
    signupstate = ''
    invitecode = ''
    with open('static/signupstate', 'r', encoding='utf-8') as f:
        signupstate = f.read()
    with open('static/invitecode', 'r', encoding='utf-8') as f:
        invitecode = f.read()
    content = cloudhead_manage+username+afterusername_manage+invitecode+aftercurrentinvitecode+signupstate+afteronregister
    tmp=''
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'select username,isadmin from '+ sqldatabase+'.user'
    check.execute(sql)
    result=check.fetchall()
    for i in result:
        if i[1]=='yes':
            isadmin='是'
        else:
            isadmin='不是'
        tmp = tmp + filedownloadurla_manage + i[0]+ filedownloadurlb_manage + '#'
        tmp = tmp + beforefilename_manage + i[0] + afterfilename_manage
        tmp = tmp + '#' + aftersize_manage + isadmin + afterfiletime_manage
    content = content + (tmp) + cloudreset_manage
    return content

def deleteuser(username):
    if username=='admin':
        return 0
    ####系统默认账号，无法被移除。
    else:
        db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
        check = db.cursor()
        sql =  'delete  from '+sqldatabase+'.user where username=' + "'" + username + "'"
        check.execute(sql)
        db.commit()
        db.close()
        return 1

def adduser(username,passwd):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql='select username from '+sqldatabase+'.user where username ='+"'"+username+"'"
    check.execute(sql)
    a=check.fetchone()
    a=list(str(a).replace('(','').replace(')','').replace("'","").split(','))
    if a[0]==username:
        print (a[0])
        return 0
    else:
        print (a[0])
        #by default we think this is not a admin, or we can add choice on add user. Maybe it would be the next step
        sql = "insert into simpledrive.user (username,passwd,md5,isadmin) VALUES (" + "'" + username + "'" + "," + "'" + passwd + "'" + "," + "'" + md5(passwd) + "'" + "," + "'" + 'no'  "'" + ")"
        check.execute(sql)
        db.commit()
        db.close()
        try:
            os.mkdir(os.getcwd() + '/cloud/' + username)
        except:
            return 2
        return 1