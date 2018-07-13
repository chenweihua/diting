#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
@version: ??
@author: chenwh
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: jenkins-tool.py.py
@time: 18-7-13 上午5:19
"""

import jenkins

url = 'http://192.168.9.120:8080'
username = 'admin'
password = '888888'

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

job_name = "www.linuxhub.org"

# 构建项目
print
server.build_job(job_name)

# 获取项目相关信息
# print server.get_job_info(job_name)

# 获取项目最后次构建号
build_number = server.get_job_info(job_name)['lastBuild']['number']
print
build_number

# 获取下一项目构建号
next_build_number = server.get_job_info(job_name)['nextBuildNumber']
print
next_build_number

# 某次构建的执行结果状态
print
server.get_build_info(job_name, build_number)['result']

# 是否构建中
print
server.get_build_info(job_name, build_number)['building']
# 构建项目


# !/usr/bin/env python
# encoding:utf8
# author: zeping lai

# pip install python-jenkins

import jenkins

url = 'http://192.168.8.53:8080'
username = 'admin'
password = '888888'

job_name = "www.linuxhub.org"

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

# 获取下一项目构建号
next_build_number = server.get_job_info(job_name)['nextBuildNumber']

# 构建项目
output = server.build_job(job_name)

# 定时10秒
from time import sleep;

sleep(10)

build_info = server.get_build_info(job_name, next_build_number)

status = build_info['result']

if status == "SUCCESS":
    print
    "构建成功：%s | 构建项目编号：%s" % (job_name, next_build_number)
else:
    print
    "构建出错: %s" % job_name


import jenkins

url = 'http://192.168.8.53:8080'
username = 'admin'
password = '888888'

job_name = "www.linuxhub.org"

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

# 获取下一项目构建号
next_build_number = server.get_job_info(job_name)['nextBuildNumber']

# 构建项目
output = server.build_job(job_name)

# 定时10秒
from time import sleep;

sleep(10)

build_info = server.get_build_info(job_name, next_build_number)

status = build_info['result']

if status == "SUCCESS":
    print
    "构建成功：%s | 构建项目编号：%s" % (job_name, next_build_number)
else:
    print
    "构建出错: %s" % job_name