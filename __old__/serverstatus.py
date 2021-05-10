#!/usr/bin/python
# coding:utf-8

##this is where we place disk usage and free usage

import os
import psutil
import platform


def returnsysteminfo():
    platinfo=''
    path = os.getcwd()
    if platform.system() == 'Windows':
        platinfo=('操作系统：Windows')
    elif platform.system() == 'Linux':
        platinfo='操作系统：Linux'


    currentdirdiskinfo=psutil.disk_usage(path)
    diskwarn='<br>以下是磁盘信息/单位（G）<br>'
    info = psutil.virtual_memory()
    usedmem = (u'内存已使用：', info.used / 1024 / 1024, 'M')
    totalmem = (u'总内存：', info.total / 1024 / 1024, 'M')
    memper = (u'内存占比：', info.percent)
    numcpu = (u'cpu个数：', psutil.cpu_count())
    systeminfo='<meta http-equiv="refresh" content="5">以下是系统信息(每隔5秒自动刷新)：<br>'
    Daemoninfo='<br>守护进程信息:<br>'
    Daemon='待添加'
    return systeminfo+str(platinfo)+'<br>'+str(usedmem + totalmem + memper + numcpu)+Daemoninfo+Daemon+diskwarn+'总计:'+str(currentdirdiskinfo[0]/1024/1024/1024)+' 已用:'+str(currentdirdiskinfo[1]/1024/1024/1024)+' 剩余: '+str(currentdirdiskinfo[2]/1024/1024/1024)+' 已用比例:'+str(currentdirdiskinfo[3])


def rebootserver():
    platinfo=''
    path = os.getcwd()
    if platform.system() == 'Windows':
        os.system('shutdown -r -t 0')

    elif platform.system()=='Linux':
        os.system('reboot')

    return ('重启完毕')

def onBoot():
    with open('/etc/rc.local', 'r') as f:
        b=f.read()
        if b.find('nohup python3 /openvpn/main.py > /openvpn/main.log 2>&1 &'):
            return 0
        else:
            with open('/etc/rc.local', 'r') as f:
                f.write('\nnohup python3 /openvpn/main.py > /openvpn/main.log 2>&1 &')
                return 1





