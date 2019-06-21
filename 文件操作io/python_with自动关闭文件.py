#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import codecs
with codecs.open("python_pathlib.py",'r','utf-8',buffering=True) as f:
    for line in f:
        print(line,end='')