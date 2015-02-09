#!/usr/bin/python 
#-*- coding: utf-8 -*-
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)


if __name__=='__main__':
    cmd = ['wget http://url/update.sh -O update.sh && chmod +x update.sh && ./update.sh']#你要执行的命令列表
    username = "root"  #用户名
    passwd = "root"    #密码
    threads = []   #多线程
    print "Begin......"
#    ssh2('192.168.1.112',username,passwd,['date','touch 2','ls'])
    for i in range(0,255):
        ip = '10.1.150.'+str(i)
        threads.append(threading.Thread(target=ssh2,args=(ip,username,passwd,cmd)))
    for i in threads:
        i.start()
    for  i in threads:
        i.join()
    print "更新完成"
