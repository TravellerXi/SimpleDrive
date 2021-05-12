#!/usr/bin/env python3
# coding:utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory
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
    import os
    path = os.getcwd() + '/lib/' + 'pan'
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