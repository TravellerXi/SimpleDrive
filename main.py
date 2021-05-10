#!/usr/bin/python
# coding:utf-8
import shutil
from flask import Flask,request,session,redirect,Response
from flask import send_from_directory
from login import *
from thisistest import *
from update import *
import os
import time
import time
from thisdef import *
from share import *
#from sharehtml import *
from manage import *
from serverstatus import *
basedir = os.path.abspath(os.path.dirname(__file__))

app =Flask(__name__)

@app.route('/cloud',methods=['GET'])
def cloud_redirect():
    username=request.cookies.get('username')
    md5credit=request.cookies.get('credit')
    if Checkmd5(md5credit,username)==0:
        return redirect('/login')
    else:
        return redirect('/folder')



@app.route('/folder',methods=['GET'])
def cloud_get():
    username =request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        print(Checkmd5(md5credit, username))
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username
        return (ReturnContentForCloud_ForcurrentFolder(path, username, ''))



@app.route('/folder/<path:folders>',methods=['GET'])
def cloud_folder_get(folders):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) ==0:
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username + '/' + folders
        #TODO 修改ReturnContentForCloud_ForcurrentFolder 方法
        return (ReturnContentForCloud_ForcurrentFolder(path, username, folders))




@app.route('/file/<path:filename>',methods=['GET'])
def file_get(filename):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username
        nextpath = checkFilenameAndFolder(filename)[1]
        path1 = path + '/' + nextpath

        thisisfilename = checkFilenameAndFolder(filename)[0]
        if thisisfilename[0:1] == ' ':
            if nextpath == 'nodirhere':
                return send_from_directory(path, filename=thisisfilename[1:], as_attachment=True)
            else:
                return send_from_directory(path1, filename=thisisfilename[1:], as_attachment=True)
        else:
            if nextpath == 'nodirhere':
                return send_from_directory(path, filename=thisisfilename, as_attachment=True)
            else:
                return send_from_directory(path1, filename=thisisfilename, as_attachment=True)



@app.route('/login', methods=['GET'])

def signin_form():
    return (loginhtm)

@app.route('/login', methods=['POST'])
def login_post():
    username = str(request.form['username'])
    password = str(request.form['password'])
    from User import User
    from ErrorCode import UserNameError, PasswdError
    LoginResult=User.login(username,password)
    if LoginResult==UserNameError or LoginResult==PasswdError:
        return (('error') + '<p>用户名或密码错误</p><br><a href="/login">返回登录</a>')
    else:
        credit=LoginResult
        response = redirect('/folder')
        response.set_cookie('username', username, max_age=7 * 24 * 3600)
        response.set_cookie('credit', credit, max_age=7 * 24 * 3600)
        return response


@app.route('/lib/<path:filename>',methods=['GET'])
def lib_get(filename):
    path = os.getcwd() + '/' + 'lib'
    nextpath = checkFilenameAndFolder(filename)[1]
    path1 = path + '/' + nextpath
    thisisfilename = checkFilenameAndFolder(filename)[0]
    if thisisfilename[0:1] == ' ':
        if nextpath == 'nodirhere':
            return send_from_directory(path, filename=thisisfilename[1:], as_attachment=True)
        else:
            return send_from_directory(path1, filename=thisisfilename[1:], as_attachment=True)
    else:
        if nextpath == 'nodirhere':
            return send_from_directory(path, filename=thisisfilename, as_attachment=True)
        else:
            return send_from_directory(path1, filename=thisisfilename, as_attachment=True)


@app.route('/pan/<path:filename>',methods=['GET'])
def pan_get(filename):
    path = os.getcwd() + '/lib/' + 'pan'
    nextpath = checkFilenameAndFolder(filename)[1]
    path1 = path + '/' + nextpath
    thisisfilename = checkFilenameAndFolder(filename)[0]
    if thisisfilename[0:1] == ' ':
        if nextpath == 'nodirhere':
            return send_from_directory(path, filename=thisisfilename[1:], as_attachment=True)
        else:
            return send_from_directory(path1, filename=thisisfilename[1:], as_attachment=True)
    else:
        if nextpath == 'nodirhere':
            return send_from_directory(path, filename=thisisfilename, as_attachment=True)
        else:
            return send_from_directory(path1, filename=thisisfilename, as_attachment=True)



@app.route('/folder/pan/<path:filename>',methods=['GET'])
def folder_pan_get(filename):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        return redirect('/pan/' + filename)


@app.route('/', methods=['GET'])
def login_firstpage():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        return redirect('/folder')

@app.route('/test',methods=['GET'])
def test_get():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        return (testdata)

@app.route('/test',methods=['post'])
def test_POST():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        if request.form['submit'] == '提交':
            print('that is awsome')
        else:
            if request.form['submit'] == '删除':
                print('that is cool')

        mycheck = request.form.getlist('mycheck')
        print(mycheck)
        mycheck = request.form.getlist('mycheck')
        for i in mycheck:
            if i[0:1] == ' ':
                i = i[1:]
            print(i)
        return redirect('/cloud')


@app.route('/folder/<path:folders>', methods=['POST'])
def folderpath_POST(folders):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username + '/' + folders
        pathtemp = path + '/'
        if request.form['formname'] == 'fileorfolderlist':
            mycheck = request.form.getlist('mycheck')
            if request.form['submit'] == '删除':
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    try:
                        os.remove(pathtemp + i)
                    except:
                        shutil.rmtree(pathtemp + i)
                return ('删除完毕<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))

            elif request.form['submit'] == '分享':
                fenxiang = 1
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    pathshare = pathtemp + i
                    fenxiang = sharefileorfolder(path + '/', username, i)
                if fenxiang == 0:
                    return ('该文件/文件夹已经分享过了<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
                else:
                    return ('分享成功,请去已分享查询<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
        elif request.form['formname'] == 'search':
            pathsearch = path
            #print(pathsearch)
            searchinfo=request.form['search']
            b=searchfilename(searchinfo,pathsearch,username)
            return (b)



        elif request.form['formname'] == 'newfile':
            path = os.getcwd() + '/cloud/' + username + '/' + folders
            file = request.files.get('file')
            pathwithfilename = path + '/' + file.filename
            file.save(pathwithfilename)
            return ('文件上传成功,页面应该刷新!<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
        elif request.form['formname'] == 'newfolder':
            newfolder = str(request.form['newfoldername'])
            pathnew = os.getcwd() + '/cloud/' + username + '/' + folders + '/' + newfolder
            path = os.getcwd() + '/cloud/' + username + '/' + folders
            # os.system('mkdir -p '+pathnew)
            os.mkdir(pathnew, 777)
            # print(path)
            return ('文件夹创建成功,页面应该刷新!<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
        else:
            return ('禁止调皮')


@app.route('/folder',methods=['POST'])
def folderroot_POST():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        path = os.getcwd().replace('\\', '/') + '/cloud/' + username
        pathtemp = path + '/'
        if request.form['formname'] == 'fileorfolderlist':
            mycheck = request.form.getlist('mycheck')
            if request.form['submit'] == '删除':
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    try:
                        os.remove(pathtemp + i)
                    except:
                        shutil.rmtree(pathtemp + i)

                return ('删除完毕<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))

            elif request.form['submit'] == '下载':
                return ('暂时不支持文件批量下载<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))

            elif request.form['submit'] == '分享':
                fenxiang = 1
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    pathshare = pathtemp + i
                    fenxiang = sharefileorfolder(path + '/', username, i)
                if fenxiang == 0:
                    return ('该文件/文件夹已经分享过了<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))
                else:
                    return ('分享成功,请去已分享查询<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))
        elif request.form['formname'] == 'search':
            path = os.getcwd().replace('\\', '/') + '/cloud/' + username
            searchinfo=request.form['search']
            b=searchfilename(searchinfo,path,username)
            return (b)



        elif request.form['formname'] == 'newfile':
            path = os.getcwd() + '/cloud/' + username + '/'
            file = request.files.get('file')
            pathwithfilename = path + '/' + file.filename
            # path='D:\Config'
            file.save(pathwithfilename)
            return ('文件上传成功,页面应该刷新!<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))
        elif request.form['formname'] == 'newfolder':
            newfolder = str(request.form['newfoldername'])
            pathnew = os.getcwd() + '/cloud/' + username + '/' + newfolder
            path = os.getcwd() + '/cloud/' + username
            # os.system('mkdir -p ' + pathnew)
            os.mkdir(pathnew, 777)
            # print(path)
            return ('文件夹创建成功,页面应该刷新!<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))



@app.route('/share/<folders>',methods=['GET'])
def share_get(folders):
    ifshareid = checksharebyshareid(folders)
    if ifshareid == 0:
        return ('分享链接无效！')
    elif ifshareid == 1:
        return ('这是个文件夹')
    else:
        ifshareid = list(ifshareid)
        ifshareid = list(str(ifshareid[0]).replace('(', '').replace(')', '').replace("'", '').split(','))
        ###以下解决ifshareid[1]开头带空格问题
        if ifshareid[1][0:1] == ' ':
            ifshareid[1] = ifshareid[1][1:]
        return send_from_directory(ifshareid[0], filename=ifshareid[1], as_attachment=True)


@app.route('/shared',methods=['GET'])
def shared_get():
    username=request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if checkUserislogined(md5credit,username)==0:
        return ('你没有登录,' + '''<a href="/"'>点此登录</a>''')
    else:
        path = os.getcwd() + '/cloud/' + username
        return (ReturnContentForCloud_ForcurrentFolder_share(username))

@app.route('/shared', methods=['POST'])
def sharedroot_POST():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if checkUserislogined(md5credit, username) == 0:
        return ('你没有登录,' + '''<a href="/"'>点此登录</a>''')
    else:
        path = os.getcwd().replace('\\', '/') + '/cloud/' + username
        pathtemp = path + '/'
        if request.form['formname'] == 'fileorfolderlist':
            mycheck = request.form.getlist('mycheck')
            ##永久有效思路，设validto为0，取消分享，即删除shareid存在得条目。
            if request.form['submit'] == '设为永久分享':
                for i in mycheck:
                    print(i)
                    alwaysvalid(i)

                return ('设置选定文件(夹)的永久分享完毕<br>' + ReturnContentForCloud_ForcurrentFolder_share(username))
            elif request.form['submit'] == '取消分享':
                for i in mycheck:
                    cancelshare(i)
                return ('已取消选定文件(夹)的分享<br>' + ReturnContentForCloud_ForcurrentFolder_share(username))
        elif request.form['formname']=='search':
            searchinfo = request.form['search']
            return (searchfromshared(username,searchinfo))

@app.route('/manage',methods=['GET'])
def manager_get():
    username=request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if checkUserislogined(md5credit,username)==0:
        return ('你没有登录,' + '''<a href="/"'>点此登录</a>''')
    else:
        if Checkisadmin(username) == 0:
            return ('非管理员无权访问该页面' + "<a href='/folder'>返回首页</a>")
        return (manageUserandServer(username))



@app.route('/manage',methods=['POST'])
def manage_POST():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if checkUserislogined(md5credit, username) == 0:
        return ('你没有登录,' + '''<a href="/"'>点此登录</a>''')
    else:
        if Checkisadmin(username) == 0:
            return ('非管理员无权访问该页面' + "<a href='/folder'>返回首页</a>")
        path = os.getcwd().replace('\\', '/') + '/cloud/' + username
        pathtemp = path + '/'
        if request.form['formname'] == 'userlist':
            mycheck = request.form.getlist('mycheck')
            ##永久有效思路，设validto为0，取消分享，即删除shareid存在得条目。
            if request.form['submit'] == '删除':
                for i in mycheck:
                    print(i)
                    if deleteuser(i) == 0:
                        return ('无法删除默认用户admin<br>' + manageUserandServer(username))
                    else:
                        return ('删除选定用户成功<br>' + manageUserandServer(username))
        elif request.form['formname'] == 'newuser':
            username = request.form['username']
            passwd = request.form['password']
            if adduser(username, passwd) == 0:
                return ('该用户已存在<br>' + manageUserandServer(username))
            else:
                return ('用户添加成功<br>' + manageUserandServer(username))
        elif request.form['formname'] == 'registerstatus':
            signupstate=str(request.form['registercode'])
            print(signupstate)
            with open('static/signupstate', 'w', encoding='utf-8') as f:
                f.write(signupstate)
            #print('1')
            return('开/关注册 设置成功<br>' + manageUserandServer(username))
        elif request.form['formname']=='registerbyinvitecode':
            invitecode=str(request.form['invitecode'])
            with open('static/invitecode', 'w', encoding='utf-8') as f:
                f.write(invitecode)
            return('开/关邀请码注册 设置成功<br>' + manageUserandServer(username))



@app.route('/serverstatus', methods=['GET'])
def serverstatus_get():
    notice=''
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if checkupdate()!=0:
        if checkupdate()==-1:
            notice='版本检测失败，可能是网络无法连接，请检查服务器日志。<br>'
        else:
            notice='有新版本'+str(checkupdate())+'可更新<br>'
    if checkUserislogined(md5credit, username) == 0:
        return ('你没有登录,' + '''<a href="/"'>点此登录</a>''')
    else:
        if Checkisadmin(username) == 0:
            return ('非管理员无权访问该页面' + "<a href='/folder'>返回首页</a>")
        return (notice+returnsysteminfo())

@app.route('/logout',methods=['POST','GET'])
def logout():
    response=redirect('/login')
    response.delete_cookie('username')
    response.delete_cookie('credit')
    return response
@app.route('/logedout',methods=['POST','GET'])
def logedout():
    return ('成功注销<a href="/login">返回登录</a>')


@app.route('/updateversion',methods=['GET'])
def updateversion_get():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    if Checkmd5(md5credit, username) == 0:
        return redirect('/login')

    updateversion()

    return (title_setup_pc('升级成功')+'升级成功！请返回首页<br><a href="/">返回首页</a>')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'GET':
        signupstate = ''
        invitecode = ''
        with open('static/signupstate', 'r', encoding='utf-8') as f:
            signupstate = f.read()
        with open('static/invitecode', 'r', encoding='utf-8') as f:
            invitecode = f.read()
        if str(signupstate) != '1':
            return ('管理员关闭了注册功能，请联系管理员<br><a href="/">返回首页</a>')
        else:
            if str(invitecode) == '0':
                return ("""
                    <title>注册</title><form action="/signup" method="post">
                    <input type="hidden" style="visibility: hidden;" name="formname" value="usernamepasswd" />

                                      <p>用户名：<input name="username"></p>

                                      <p>密码：&nbsp&nbsp&nbsp<input name="password" type="password"></p>

                                      <p><button type="submit">注册</button></p>

                                      </form>

                    """)
            else:
                return(
                """

                <title>注册</title><form action="/signup" method="post">
                <input type="hidden" style="visibility: hidden;" name="formname" value="invitecode" />

                                  <p>用户名：<input name="username"></p>

                                  <p>密码：&nbsp&nbsp&nbsp<input name="password" type="password"></p>

                                  <p>邀请码：<input name="invitecode"></p>

                                  <p><button type="submit">注册</button></p>

                                  </form>

                """)
    if request.method=='POST':
        if request.form['formname']=='usernamepasswd':
            username=request.form['username']
            password=request.form['password']
            if adduser(username, password) == 0:
                return ('该用户已存在，无法注册<br>' + '<a href="/signup">点此重新注册</a>')
            else:
                return ('注册成功 <br><a href="/">点此登录</a>')
        elif request.form['formname']=='invitecode':
            username = request.form['username']
            password = request.form['password']
            incominginvitecode=request.form['invitecode']
            invitecode=''
            with open('static/invitecode', 'r', encoding='utf-8') as f:
                invitecode = f.read()
            if incominginvitecode==invitecode:
                adduser(username,password)
            return ('注册成功 <br><a href="/">点此登录</a>')

@app.route('/favicon',methods=['GET'])
def get_fav():

    return app.send_static_file('favicon.png')



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80, debug=True,threaded=True)
