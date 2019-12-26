#!/usr/bin/python

# coding:utf-8
import os
import time

from flask import Flask,request,session,redirect,Response

from flask import send_from_directory

import os
from folder import *
from sharehtml import *
from searchhtml import *
import pymysql

sqlservername='localhost'
sqluser='simpledrive'
sqlpasswd='simpledrive'
sqldatabase='simpledrive'



def searchfilename(filename,path,username):
    thisfiles=''
    thisroot=''
    thisdirs=''
    a=[]
    c = []
    for root, dirs, files in os.walk(path, topdown=True, onerror=None, followlinks=False):
        b=[]
        thisfiles=str(files)
        thisroot=str(root)
        thisdirs=str(dirs)
        b.append(thisroot)
        b.append(thisfiles)
        b.append(thisdirs)
        a.append(b)
    #print(a)
    #print(path)
    #c is the result for file/folde and dir
    for i in a:
        if i[1].find(filename)!=-1:
            #print(i[1])
            q=list(i[1].replace('[','').replace(']','').split('"'))
            #print(q)
            for n in q:
                #print(n)
                if n.find(filename)!=-1:
                    #print(n)
                    y=list(n.replace("'",'').split(','))
                    #print(y)
                    for x in y:
                        #print(x)
                        if x.find(filename)!=-1:
                            #print(x)
                            d = []
                            temppath = i[0]
                            tempfile = x
                            d.append(temppath)
                            d.append(tempfile)
                            c.append(d)
        if i[2].find(filename) != -1:
            # print(i[1])
            q = list(i[2].replace('[', '').replace(']', '').split('"'))
            # print(q)
            for n in q:
                # print(n)
                if n.find(filename) != -1:
                    # print(n)
                    y = list(n.replace("'", '').split(','))
                    # print(y)
                    for x in y:
                        # print(x)
                        if x.find(filename) != -1:
                            # print(x)
                            d = []
                            temppath = i[0]
                            tempfile = x
                            d.append(temppath)
                            d.append(tempfile)
                            c.append(d)
    efolder = []
    ffilename = []
    for i in c:
        efolder.append(i[0])
        ffilename.append(i[1])
    #print(efolder)
    #print(ffilename)
    #returnsearchhtml(efolder,username,username)

    return (returnsearchhtml(efolder,ffilename,username))

#folderandfile=searchfilename('关机','C:\\Users\\Quantdo\\OneDrive\\工作\\SimpleDrive\\cloud\\admin','admin')
#print(folderandfile)



def ReturnContentForCloud(path,username):
    content = """<table border="1">"""
    if ReturnNextDir(path)==0:
        content=content+'<tr><td>此文件夹下目前没有文件夹</td></tr><br>'
    else:
        for i in ReturnNextDir(path):
            #i=i.replace(' ','')
            #i=handlePathto(i)
            i=i.replace(' ','')
            # print('folders are' + i)
            content = content + ("""<tr><td><a href='/folder/""" + i + """'target='_blank'>""" + """Folders:""" + i + """</a></td></tr>""")
            # print(i)
    if ReturnCurrentPathFiles(path) ==0:
        content=content+'No Files here<br>'
    else:
        for i in ReturnCurrentPathFiles(path):
            #i = i.replace(' ', '')
            i=handlePathto(i)
            content = content + (
                    """<tr><td><a href='file""" + ReturnFileUrl(path,username) + """/""" + i + """'target='_blank'>""" + """files:""" + i + """</a></td></tr>""")

    content = content + ('</table>')
    content = content + ("""<p>在此目录上传新文件>>></p>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=点此上传>
        </form>""")
    content = content + ("""<br><p>新建文件夹>>></p>
            <form  method="post">

                                  <p>文件夹名：<input name="newfoldername"></p>
                                <p><button type="submit">提交</button></p></form>""")


def ReturnNextDir(path):
    b = str(file_name_dirs_root(path)[2]).replace('[', '').replace(']', '').replace("'", "")
    NextDir = b.split(',')
   # if NextDir is not True:
    #    return 0
    #else:
    #print(NextDir)
    return (NextDir)


def file_name_dirs_root(file_dir):
    thisfiles=''
    thisroot=''
    thisdirs=''
    for root, dirs, files in os.walk(file_dir, topdown=False, onerror=None, followlinks=False):
        thisfiles=str(files)
        thisroot=str(root)
        thisdirs=str(dirs)
    return (thisfiles, thisroot, thisdirs)
    
    




###disable it for test purpose
def checkUserislogined(md5,username):
    if username is None:
        return 0
    else:
        if md5 is None:
            return 0
        else:
            if Checkmd5(md5, username) < 1:
                return 0
            else:
                return 1

#def checkUserislogined(md5,username):
 #   return 1



def ReturnCurrentPathFiles(path):
    currentPathFilename=str(file_name_dirs_root(path)[0])
    a = currentPathFilename.replace('[', '').replace(']', '').replace("'", "")
    Filelist = a.split(',')
    return  Filelist





def Checkmd5(md5,username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select md5 from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if md5 == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def ReturnUserlist():

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select username from openvpn.user'

    check.execute(usernameSQL)

    Strcheck = str(check.fetchall())

    Strcheck = Strcheck.replace('(', '').replace(')', '').replace(',', '').replace("'", '')

    return (Strcheck)











def Checkisadmin(username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select isadmin from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if result=='yes':

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckUsername(username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select username from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if username == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckPassword(username,password):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    passwordSQL = 'select password from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(passwordSQL)

    if check.fetchone() is None:

        db.close()

        return 0

    else:

        check.execute(passwordSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if password == result:

            db.close()

            return 2

        else:

            db.close()

            return 0



def inviteC():

    with open('static/invitecode','r',encoding='utf-8') as f:

        return(f.read())



#def checkUserislogined(md5,username):
#    if username is None:
    #       return 0
        #   else:
        #      if md5 is None:
        #          return 0
        #    else:
        #          if Checkmd5(md5, username) < 1:
        #        return 0
        #        else:
#       return 1






def Checkmd5(md5,username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    try:
        usernameSQL = 'select md5 from '+sqldatabase+'.user where username=' + "'" + username + "'"
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





def ReturnUserlist():

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select username from '+sqldatabase+'.user'

    check.execute(usernameSQL)

    Strcheck = str(check.fetchall())

    Strcheck = Strcheck.replace('(', '').replace(')', '').replace(',', '').replace("'", '')

    return (Strcheck)











def Checkisadmin(username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select isadmin from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if result=='yes':

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckUsername(username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select username from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if username == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckPassword(username,password):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    passwordSQL = 'select password from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(passwordSQL)

    if check.fetchone() is None:

        db.close()

        return 0

    else:

        check.execute(passwordSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if password == result:

            db.close()

            return 2

        else:

            db.close()

            return 0



def inviteC():

    with open('static/invitecode','r',encoding='utf-8') as f:

        return(f.read())



def returnsearchhtml(path,filename,username):
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


def ReturnContentForCloud_ForcurrentFolder(path,username,currentfolder):
    content = cloudhead+username+preusername
    ###try to close the door for non-admin user.
    if Checkisadmin(username)>0:
        content=content+adminpage+afteradminpage
    else:
        content=content+afteradminpage
    if ''.join(ReturnNextDir(path)).replace("'","")  =='':
        content = content + '<tr><td>此文件夹下目前没有文件夹</td></tr><br>'
    else:
        for i in ReturnNextDir(path):
            if currentfolder=='':
                if i[0:1]==' ':
                    i=i[1:]
                    i=i.replace(' ','')
                    tmp = filedownloadurla+i+filedownloadurlb + "/folder/" + i
                    tmp = tmp + beforefilename + '文件夹：' + i + afterfilename
                    tmp=tmp+getfolderorfilesize(path+'/','')+aftersize+getfilecreatetime(path+'/','')+afterfiletime
                    content = content + (tmp)
                else:
                    tmp = filedownloadurla+i+filedownloadurlb + "/folder/" + i
                    tmp = tmp + beforefilename + '文件夹：' + i + afterfilename
                    tmp = tmp + getfolderorfilesize(path +  '/' , '') + aftersize+getfilecreatetime(path+'/','')+afterfiletime
                    content = content + (tmp)
            else:
                i = i.replace(' ', '')
                tmp = filedownloadurla+i+filedownloadurlb + "/folder/"+currentfolder+"/"
                tmp = tmp + i
                tmp = tmp + beforefilename + '文件夹：' + i + afterfilename
                tmp = tmp + getfolderorfilesize(path +  '/' , '') + aftersize+getfilecreatetime(path+'/','')+afterfiletime
                content = content + (tmp)
    if ReturnCurrentPathFiles(path) ==0:
        content = content + 'No Files here<br>'
    else:
        for i in ReturnCurrentPathFiles(path):
            print(i)
            if currentfolder=='':
                if i=='':
                    content = content + (
                            """<tr><td>此文件夹目前没有文件</td></tr>""")
                else:
                    if i[0:1]==' ':
                        i=i[1:]
                    tmp=filedownloadurla+i+filedownloadurlb+"'"+"/file/"+i
                    tmp=tmp+"'"
                    tmp=tmp+beforefilename+  '文件：'+i  +afterfilename
                    tmp = tmp + getfolderorfilesize(path +'/' , i) + aftersize+getfilecreatetime(path+'/',i)+afterfiletime
                    content = content + (tmp)

            else:
                if i=='':
                    content = content + (
                            """<tr><td>此文件夹目前没有文件</td></tr>""")
                else:
                    if i[0:1]==' ':
                        i=i[1:]
                    tmp = filedownloadurla+i+filedownloadurlb + "/file/"+currentfolder+"/"
                    tmp=tmp+i
                    tmp = tmp + beforefilename + '文件：' + i + afterfilename
                    tmp = tmp + getfolderorfilesize(path+ '/' , i) + aftersize+getfilecreatetime(path+'/',i)+afterfiletime
                    content = content + (tmp)
    content=content+cloudreset
    return content




def ReturnContentForCloud_ForcurrentFolder_shared(path,username,currentfolder):
    content = cloudhead_shared
    if ''.join(ReturnNextDir(path)).replace("'","")  =='':
        content = content + '<tr><td>此文件夹下目前没有文件夹</td></tr><br>'
    else:
        for i in ReturnNextDir(path):
            if currentfolder=='':
                if i[0:1]==' ':
                    i=i[1:]
                    i=i.replace(' ','')
                    tmp = filedownloadurla_shared+i+filedownloadurlb_shared + "/folder/" + i
                    tmp = tmp + beforefilename_shared + '文件夹：' + i + afterfilename_shared
                    tmp=tmp+getfolderorfilesize(path+'/','')+aftersize_shared+getfilecreatetime(path+'/','')+afterfiletime_shared
                    content = content + (tmp)
                else:
                    tmp = filedownloadurla_shared+i+filedownloadurlb_shared + "/folder/" + i
                    tmp = tmp + beforefilename_shared + '文件夹：' + i + afterfilename_shared
                    tmp = tmp + getfolderorfilesize(path +  '/' , '') + aftersize_shared+getfilecreatetime(path+'/','')+afterfiletime_shared
                    content = content + (tmp)
            else:
                i = i.replace(' ', '')
                tmp = filedownloadurla_shared+i+filedownloadurlb_shared + "/folder/"+currentfolder+"/"
                tmp = tmp + i
                tmp = tmp + beforefilename_shared + '文件夹：' + i + afterfilename_shared
                tmp = tmp + getfolderorfilesize(path +  '/' , '') + aftersize+getfilecreatetime(path+'/','')+afterfiletime_shared
                content = content + (tmp)
    if ReturnCurrentPathFiles(path) ==0:
        content = content + 'No Files here<br>'
    else:
        for i in ReturnCurrentPathFiles(path):
            if currentfolder=='':
                if i=='':
                    content = content + (
                            """<tr><td>此文件夹目前没有文件</td></tr>""")
                else:
                    if i[0:1]==' ':
                        i=i[1:]
                    tmp=filedownloadurla_shared+i+filedownloadurlb_shared+"'"+"/file/"+i
                    tmp=tmp+"'"
                    tmp=tmp+beforefilename_shared+  '文件：'+i  +afterfilename_shared
                    tmp = tmp + getfolderorfilesize(path +'/' , i) + aftersize_shared+getfilecreatetime(path+'/',i)+afterfiletime_shared
                    content = content + (tmp)

            else:
                if i=='':
                    content = content + (
                            """<tr><td>此文件夹目前没有文件</td></tr>""")
                else:
                    if i[0:1]==' ':
                        i=i[1:]
                    tmp = filedownloadurla_shared+i+filedownloadurlb_shared + "/file/"+currentfolder+"/"
                    tmp=tmp+i
                    tmp = tmp + beforefilename_shared + '文件：' + i + afterfilename_shared
                    tmp = tmp + getfolderorfilesize(path+ '/' , i) + aftersize_shared+getfilecreatetime(path+'/',i)+afterfiletime_shared
                    content = content + (tmp)
    content=content+cloudreset_shared
    return content


def checkFilenameAndFolder(path):
    i = 0
    confirm = 0
    while 1:

        judge = path[confirm:].find('/')

        if judge > -1:
            confirm = confirm + judge + 1
            i = i + 1
        else:
            i = i - 1
            lastfile = path[confirm:]
            seConfirm = 0
            dirfilepath = []
            ###以下找dir
            a = 0
            while 1:

                judgeq = path[seConfirm:].find('/')

                if judgeq > -1:
                    seConfirm = seConfirm + judgeq + 1
                    dirfilepath.append(seConfirm - 1)
                    a = a + 1
                    #print(a)
                else:
                    #print('显示次数')
                    #print(a)
                    #a=int(a)
                    if a ==0:
                        #print('hereis a')
                        #print(a)
                        return (lastfile,'nodirhere')
                    else:
                        dir = []
                        temp = 0
                        whatisthehell = 0
                        while temp < (i + 1):
                            whatfuck = int((str(dirfilepath[temp:temp + 1]).replace('[', '').replace(']', '')))
                            #print('thisis what fuck: ')
                            #print(whatfuck)
                            dir.append(path[whatisthehell:whatfuck])
                            whatisthehell = whatfuck
                            temp = temp + 1
                        str1=','.join(dir)
                        str1=str1.replace(',','')
                        #print(str1)
                    return (lastfile, str1)

def handlePathto(path):
    path=path.replace('/','?')
    return path

def handlePathback(path):
    if path[0:1]==' ':
        path=path[1:]
        path = path.replace('?', '/')
        # = path.replace('%20', ' ')
    else:
        path = path.replace('?', '/')
        #path = path.replace('%20', ' ')
    return path


def ReturnFileUrl(path,username):
    longpath = str(ReturnCurrentFolder(path))
    filestr = '/openvpn/' + username
    sample=longpath.find(filestr)
    return (longpath[sample+9+len(username):])

def ReturnCurrentFolder(path):
    currentPathFolder=str(file_name_dirs_root(path)[1])
    a = currentPathFolder.replace('[', '').replace(']', '').replace("'", "")
   # if a is not True:
    #    return 0
    #else:
    return  a

def judgeiffileorfolderbyname(name):
    a=name.find('/')
    if a >0:
        return (1)
    else:
        return (2)


##also useful for folder
def getfilecreatetime(path,file):
    if file[0:1]==' ':
        file=file[1:]
        #print(file)
    createtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path+file).st_ctime))
    return createtime

def getfolderorfilesize(path,file):
    if file=='':
        path=path
    else:
        path = path + '/'
    if file[0:1]==' ':
        file=file[1:]
        #print(file)
    a = os.path.getsize(path + file)
    e = a / float(1024 * 1024)
    c = ("%.3d" % (e))
    if int(c) == 0:
        f = a / float(1024)
        return str("%.2f KB" % (f))
    else:
        d = str(int(c))+' MB'
        return (d)


##this is login security check
def logincheck(username,passwd,md5):
    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)
    check = db.cursor()
    sql = 'delete  from '+sqldatabase+'.share where shareid=' + "'" + shareid + "'"
    try:
        check.execute(sql)
        db.commit()
        db.close()
        return 1
    except:
        return 0


def CheckUsername(username):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    usernameSQL = 'select username from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if username == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckPassword(username,password):

    db = pymysql.connect(sqlservername, sqluser, sqlpasswd, sqldatabase)

    check = db.cursor()

    passwordSQL = 'select passwd from '+sqldatabase+'.user where username=' + "'" + username + "'"

    check.execute(passwordSQL)

    if check.fetchone() is None:

        db.close()

        return 0

    else:

        check.execute(passwordSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if password == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





