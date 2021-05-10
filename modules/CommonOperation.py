#!/usr/bin/env python3
# coding:utf-8

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