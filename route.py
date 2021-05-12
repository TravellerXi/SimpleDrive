#!/usr/bin/env python3
# coding:utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory
import os
import shutil
app =Flask(__name__)

@app.route('/login', methods=['GET'])
def signin_form():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_post():
    username = str(request.form['username'])
    password = str(request.form['password'])
    from modules.User import login
    from methods.ErrorCode import UserNameError, PasswdError
    LoginResult=login(username,password)
    if LoginResult==UserNameError or LoginResult==PasswdError:
        return render_template("UsernamePasswordError.html")
    else:
        credit=LoginResult
        response = redirect('/folder')
        response.set_cookie('username', username, max_age=7 * 24 * 3600)
        response.set_cookie('credit', credit, max_age=7 * 24 * 3600)
        return response

@app.route('/favicon',methods=['GET'])
def get_fav():
    return app.send_static_file('favicon.png')

@app.route('/logout',methods=['POST','GET'])
def logout():
    response=redirect('/login')
    response.delete_cookie('username')
    response.delete_cookie('credit')
    return response

@app.route('/logedout',methods=['POST','GET'])
def logedout():
    return render_template("Logedout.html")

@app.route('/', methods=['GET'])
def login_firstpage():
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        return redirect('/folder')

@app.route('/folder',methods=['GET'])
def cloud_get():
    import os
    username =request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5=md5credit, username=username) == 0:
        print(Sql.Checkmd5(md5=md5credit, username=username))
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username
        from modules.folder import ReturnContentForCloud_ForcurrentFolder
        return (ReturnContentForCloud_ForcurrentFolder(path, username, ''))

@app.route('/pan/<path:filename>',methods=['GET'])
def pan_get(filename):
    path = os.getcwd() + '/lib/' + 'pan'
    from __old__.thisdef import checkFilenameAndFolder
    nextpath = checkFilenameAndFolder(filename)[1]
    path1 = path + '/' + nextpath
    thisisfilename = checkFilenameAndFolder(filename)[0]
    # FLASK 2.0.0 更新以后，flask.send_from_directory(directory, path, **kwargs)
    if thisisfilename[0:1] == ' ':
        if nextpath == 'nodirhere':
            return send_from_directory(path, path=thisisfilename[1:], as_attachment=True)
        else:
            return send_from_directory(path1, path=thisisfilename[1:], as_attachment=True)
    else:
        if nextpath == 'nodirhere':
            return send_from_directory(path, path=thisisfilename, as_attachment=True)
        else:
            return send_from_directory(path1, path=thisisfilename, as_attachment=True)

@app.route('/lib/<path:filename>',methods=['GET'])
def lib_get(filename):
    path = os.getcwd() + '/' + 'lib'
    from __old__.thisdef import checkFilenameAndFolder
    nextpath = checkFilenameAndFolder(filename)[1]
    path1 = path + '/' + nextpath
    thisisfilename = checkFilenameAndFolder(filename)[0]
    # FLASK 2.0.0 更新以后，flask.send_from_directory(directory, path, **kwargs)
    if thisisfilename[0:1] == ' ':
        if nextpath == 'nodirhere':
            return send_from_directory(directory=path, path=thisisfilename[1:], as_attachment=True)
        else:
            return send_from_directory(path1, path=thisisfilename[1:], as_attachment=True)
    else:
        if nextpath == 'nodirhere':
            return send_from_directory(path, path=thisisfilename, as_attachment=True)
        else:
            return send_from_directory(path1, path=thisisfilename, as_attachment=True)

@app.route('/file/<path:filename>',methods=['GET'])
def file_get(filename):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        path = os.getcwd() + '/cloud/' + username
        from __old__.thisdef import checkFilenameAndFolder
        nextpath = checkFilenameAndFolder(filename)[1]
        path1 = path + '/' + nextpath

        thisisfilename = checkFilenameAndFolder(filename)[0]
        if thisisfilename[0:1] == ' ':
            if nextpath == 'nodirhere':
                return send_from_directory(path, path=thisisfilename[1:], as_attachment=True)
            else:
                return send_from_directory(path1, path=thisisfilename[1:], as_attachment=True)
        else:
            if nextpath == 'nodirhere':
                return send_from_directory(path, path=thisisfilename, as_attachment=True)
            else:
                return send_from_directory(path1, path=thisisfilename, as_attachment=True)

@app.route('/folder/pan/<path:filename>',methods=['GET'])
def folder_pan_get(filename):
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5credit, username) == 0:
        return redirect('/login')
    else:
        return redirect('/pan/' + filename)

@app.route('/folder/<path:folders>', methods=['POST'])
def folderpath_POST(folders):
    from modules.folder import ReturnContentForCloud_ForcurrentFolder, ReturnContentForCloud_ForcurrentFolder
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5credit, username) == 0:
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
                        import shutil
                        shutil.rmtree(pathtemp + i)
                from __old__.thisdef import ReturnContentForCloud_ForcurrentFolder
                return ('删除完毕<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))

            elif request.form['submit'] == '分享':
                fenxiang = 1
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    pathshare = pathtemp + i
                    from __old__.share import sharefileorfolder
                    fenxiang = sharefileorfolder(path + '/', username, i)
                if fenxiang == 0:
                    return ('该文件/文件夹已经分享过了<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
                else:
                    return ('分享成功,请去已分享查询<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, folders))
        elif request.form['formname'] == 'search':
            pathsearch = path
            #print(pathsearch)
            searchinfo=request.form['search']
            from __old__.thisdef import searchfilename
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
    from __old__.thisdef import ReturnContentForCloud_ForcurrentFolder
    username = request.cookies.get('username')
    md5credit = request.cookies.get('credit')
    from modules.Sql import SqlMethod
    Sql=SqlMethod()
    if Sql.Checkmd5(md5credit, username) == 0:
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

                from __old__.thisdef import ReturnContentForCloud_ForcurrentFolder
                return ('删除完毕<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))

            elif request.form['submit'] == '下载':
                from __old__.thisdef import ReturnContentForCloud_ForcurrentFolder
                return ('暂时不支持文件批量下载<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))

            elif request.form['submit'] == '分享':
                fenxiang = 1
                for i in mycheck:
                    if i[0:1] == ' ':
                        i = i[1:]
                    pathshare = pathtemp + i
                    from __old__.share import sharefileorfolder
                    fenxiang = sharefileorfolder(path + '/', username, i)
                if fenxiang == 0:
                    return ('该文件/文件夹已经分享过了<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))
                else:
                    return ('分享成功,请去已分享查询<br>' + ReturnContentForCloud_ForcurrentFolder(path, username, ''))
        elif request.form['formname'] == 'search':
            path = os.getcwd().replace('\\', '/') + '/cloud/' + username
            searchinfo=request.form['search']
            from __old__.thisdef import searchfilename
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

