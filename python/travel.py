#!/usr/bin/python
import os
i=0
def travel(dirpath,callback,deps=0):
    """
    dirpath:要遍历的目录路径
    callback:回调函数
    deps:遍历层级，当deps=0时全部遍历，不限制遍历深度
    """
    global i
    if deps != 0 and i >= deps:
        return
    files =  os.listdir(dirpath)
    for subfile in files:
        new_file=dirpath + '/' + subfile
        if new_file[0] == '.':
            pass
        if os.path.isdir(new_file):
            i = i + 1
            travel(new_file,callback,deps)
        else:
            callback(new_file)
#回调函数
def callback(f_name):
    print f_name
travel(".",echo,deps=0)
