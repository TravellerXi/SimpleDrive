#!/usr/bin/python

# coding:utf-8
import pymysql
import os
#path = os.getcwd() + '/' + username + '/' + folders
import random
import string
import time
import datetime
from sharehtml import *
from thisdef import *
from search_share_html import *


def checksharebyshareid(shareid):
    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check = db.cursor()
    sql = 'select relativepostion,fileorfoldername,path from simpledrive.share where shareid=' + "'" + shareid + "'"
    check.execute(sql)
    if (check.fetchone()) is None:
        db.close()
        return 0
    else:
        ##该用户没有share
        check.execute(sql)
        result = check.fetchall()
        resulttep=list(result)
        resulttep=str(resulttep).replace('(','').replace(')','').replace('[','').replace(']','')
        resulttep=list(resulttep.split(','))
        if resulttep[2][0:1]==' ':
            resulttep[2]=resulttep[2][1:]
        resulttep[2]=resulttep[2].replace("'",'')
        print('resulttep[2] is',resulttep[2])

        if checkfileorfolder(resulttep[2])==1:
            return 1
        else:
            return result


def checkfileorfolderalreadyexistinshare(path):
    db=pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check=db.cursor()
    sql='select * from simpledrive.share where path=' + "'" + path + "'"
    check.execute(sql)
    if (check.fetchone()) is None:

        db.close()

        return 0

    else:
        return 1

def CheckShareidSql(shareidsql):

    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')

    check = db.cursor()

    SQL = 'select shareid from simpledrive.share where shareid=' + "'" + shareidsql + "'"

    check.execute(SQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(SQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if shareidsql == result:

            db.close()

            return 2

        else:

            db.close()

            return 0

def generateshareid():
    i=1;r=''
    s = string.ascii_lowercase
    number=random.randint(999, 9999999)
    while i<10:
        r=r+random.choice (s)
        i=i+1
    randomnumber=r+str(number)
    return randomnumber


def checkfileorfolder(path):
    if os.path.isdir(path):
        return 1#folder
    else:
        return 2#file

def sharefileorfolder(path,username,filename):
    #print(path)
    #print(path+filename)
    if checkfileorfolderalreadyexistinshare(path+filename)==0:
        db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
        check = db.cursor()
        if checkfileorfolder(path+filename) == 1:
            username = username
            path1 = path+filename
            print(path1)
            c='''\\'''
            path1=str(path1).replace(c,'/')
            relativepostion = str(path).replace(c,'/')
            isdir = 'yes'
            validto = sevendaysshijianchuo()
            downloadedtime = '0'
            entercode = ''
            shareid = ''
            fileorfoldername=filename
            while 1:
                shareid = generateshareid()
                if CheckShareidSql(shareid) == 0:
                    break
                else:
                    print('还没结束1')
            print('#1',path1)
            sqlpha = "insert into simpledrive.share (username,path,shareid,validto,downloadedtime,entercode,isdir,relativepostion,fileorfoldername) VALUES (" + "'" + username + "'" + "," + "'" + path1 + "'" + "," + "'" + shareid + "'" + "," + "'" + validto + "'" + "," + "'" + downloadedtime + "'" + "," + "'" + entercode + "'" + "," + "'" + isdir + "'""," + "'" + relativepostion + "'""," + "'" + fileorfoldername + "'" + ")"
            # print(sqlpha)
            check.execute(sqlpha)
            db.commit()
            check.close()
        else:
            username = username
            path1 = path+filename
            c = '''\\'''
            path1 = str(path1).replace(c, '/')
            isdir = 'no'
            validto = sevendaysshijianchuo()
            downloadedtime = '0'
            entercode = ''
            shareid = ''
            relativepostion = str(path).replace(c,'/')
            fileorfoldername=filename
            while 1:
                shareid = generateshareid()
                if CheckShareidSql(shareid) == 0:
                    break
                else:
                    print('还没结束2')
            print('#2',path1)
            #print('relativepostion is: ',relativepostion)
            sqlpha = "insert into simpledrive.share (username,path,shareid,validto,downloadedtime,entercode,isdir,relativepostion,fileorfoldername) VALUES (" + "'" + username + "'" + "," + "'" + path1 + "'" + "," + "'" + shareid + "'" + "," + "'" + validto + "'" + "," + "'" + downloadedtime + "'" + "," + "'" + entercode + "'" + "," + "'" + isdir + "'""," + "'" + relativepostion + "'""," + "'" + fileorfoldername + "'" + ")"
            # print(sqlpha)
            check.execute(sqlpha)
            db.commit()
            check.close()
        return 1
    else:
        return 0

def sevendaysshijianchuo():
    now = datetime.datetime.now()
    dangqianshijian = datetime.datetime.strptime(now.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=7)
    sevendaylatertime = dangqianshijian + delta
    sevendaylatertime_shijianchuo = time.mktime(sevendaylatertime.timetuple())
    return  str(sevendaylatertime_shijianchuo)


def checksharedbyusername(username):
    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check=db.cursor()
    sql='select path,shareid,validto,downloadedtime,entercode,isdir,relativepostion,fileorfoldername from simpledrive.share where username=' + "'" + username + "'"
    check.execute(sql)
    n=0
    if (check.fetchone()) is None:
        db.close()
        return 0
    ##该用户没有share
    else:
        check.execute(sql)
        result=check.fetchall()
        #print(result)
        return result

def ReturnContentForCloud_ForcurrentFolder_share(username):
    result=checksharedbyusername(username)
    content = cloudhead_shared+username+preusername_shared
    if Checkisadmin(username)>0:
        content=content+adminpage_shared+afteradminpage_shared
    else:
        content=content+afteradminpage_shared
    tmp=''
    if checksharedbyusername(username)==0:
        content=content+'当前用户没有分享'
    else:
        for i in result:
            realpathwithfilename=i[0]
            sharedid=i[1]
            validto=i[2]
            downloadedtime=i[3]
            entercode=i[4]
            isdir=i[5]
            relativepostion=i[6]
            #print(relativepostion)
            fileorfoldername=i[7]
            sharelink=sharedid
            dirtype=''
            currentposition='SimpleDrive/cloud/'+username
            lenofusername=len(username)
            thisislocation=relativepostion.find(currentposition)
            #print(thisislocation)
            xiangduiposition=relativepostion[thisislocation+18+lenofusername:]
            #xiangduiposition=xiangduiposition[xiangduiposition.find('/'):]
            #print(xiangduiposition)
            if int(float(validto))==0:
                validto='永久有效'
            else:
                if time.time()>int(float(validto)):
                    validto='分享已过期'
                else:
                    dateArray = datetime.datetime.fromtimestamp(int(float(validto)))
                    validto = dateArray.strftime("%Y--%m--%d %H:%M:%S")
            if entercode=='':
                entercode='无密码'
            if isdir=='yes':
                dirtype='文件夹'
            else:
                dirtype='文件'
            tmp =tmp+ filedownloadurla_shared + sharedid + filedownloadurlb_shared + '/share/'+sharelink
            tmp = tmp + beforefilename_shared +fileorfoldername + afterfilename_shared+dirtype+afterposition_shared+xiangduiposition+position
            tmp = tmp + getfolderorfilesize(realpathwithfilename, '') + aftersize_shared + validto + afterfiletime_shared
    content = content + (tmp)+cloudreset_shared
    return content

def alwaysvalid(shareid):
    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check = db.cursor()
    sql =  'update simpledrive.share set validto =0 where shareid=' + "'" + shareid + "'"
    try:
        check.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        return 0



def cancelshare(shareid):
    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check = db.cursor()
    sql = 'delete  from simpledrive.share where shareid=' + "'" + shareid + "'"
    try:
        check.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        return 0

def searchfromshared(username,searchcontent):
    db = pymysql.connect('localhost', 'simpledrive', 'simpledrive', 'simpledrive')
    check = db.cursor()
    sql = 'select relativepostion,fileorfoldername from simpledrive.share where username=' + "'" + username + "'"
    check.execute(sql)
    listforpathandfilename=[]
    efolder = []
    ffilename = []
    if (check.fetchone()) is None:
        db.close()
        return 0
    else:
        ##该用户没有share
        check.execute(sql)
        result = check.fetchall()
        #print(result)
        for i in result:
            if i[1].find(searchcontent)!=-1:
                efolder.append(i[0] [:-1])
                print(efolder)
                ffilename.append(i[1])
    #print(efolder)
    return (returnsearchhtmlforshare(efolder,ffilename,username))


def returnsearchhtmlforshare(path,filename,username):
    #print(path)
    #print(type(path))
    content = cloudhead_search + username + preusername_search
    ###try to close the door for non-admin user.
    if Checkisadmin(username) > 0:
        content = content + adminpage_search + afteradminpage_search
    else:
        content = content + afteradminpage_search
    count=0
    tempath=os.getcwd()+'/'+username
    for i in path:
        i=i.replace('\\','/')
        #print(i)
        tmp = filedownloadurla_search + '' + filedownloadurlb_search  + '/folder'+i[len(tempath)+len(username)+1:]
        #print('alert:')
        #print(i[len(tempath)+len(username)+1:])
        tmp = tmp + beforefilename_search  + filename[count]  + afterfilename_search
        tmp = tmp + getfolderorfilesize(i+'/',filename[count]) + aftersize_search + getfilecreatetime(i+'/',filename[count]) + afterfiletime_search
        content = content + (tmp)
        count=count+1

    content = content + cloudreset_search
    return content

