# -*- coding: utf-8 -*-
#########################################################################
# File Name: file_filter.py
# Author: Hejun Xu
# mail: 1124418652@qq.com
# Created Time: 2018年10月30日 星期二 20时40分00秒
#########################################################################
#! usr/bin/env python

import re
import os
import sys

def isCodeFile(filename):
    if os.path.splitext(filename)[1].lower() in ['.py', '.ipynb', '.h', '.csv', '.txt']:
        return True
    return False

def findIgnoreFile(path):
    tmp_path = path
    ignore_file = []

    if os.path.isfile(path) and not isCodeFile(path):
        ignore_file.append(path)

    elif os.path.isdir(path):
        for name in os.listdir(tmp_path):
            tmp_path = os.path.join(path, name)
            ignore_file.extend(findIgnoreFile(tmp_path))

    return ignore_file

def findAllFile(path):
    file_list = []

    if os.path.isfile(path):
        file_list.append(path)
    else:
        for name in os.listdir(path):
            tmp_path = os.path.join(path, name)
            file_list.extend(findAllFile(tmp_path))

    return file_list

def modify(basePath, file_list, appdir):
    if os.path.isdir(appdir):
        file_list.extend(findAllFile(appdir))
    
    for index, val in enumerate(file_list):
        file_list[index] = val[len(basePath)+1:]

    return file_list

def write_to_file(path, file_list):
    with open(path, "w+") as fw:
        for i in file_list:
            fw.write(i + "\n")
    


def main():
    basePath = os.getcwd()
    ignorePath = os.path.join(basePath, ".gitignore")
    appdir = os.path.join(basePath, "kaggle-cli")
    file_list = modify(basePath, findIgnoreFile(basePath), appdir)
    write_to_file(ignorePath, file_list)

if __name__ == "__main__":
    main()
