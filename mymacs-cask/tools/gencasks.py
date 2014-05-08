#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''读取.rb文件，生成python可读到的ini文件
'''
import os
import sys
from ConfigParser import RawConfigParser

def genconfig(filename):
	"""读取文件，取得数据内容，生成词典
	"""
	with open(filename, "r") as f:
		read_rb = f.read()

	lines = read_rb.split("\n")
	url = lines[1].lstrip()[len("url '"):-1]
	homepage = lines[2].lstrip()[len("homepage '"):-1]
	version = lines[3].lstrip()[len("version '"):-1]
	link = lines[5].lstrip()[len("link '"):-1]
	## 每个文件内容，生成一个字典内容
	d = {
		"url": url,
		"homepage": homepage,
		"version": version,
		"link": link}

	return d

def write_config(d, filename):
	"""将信息写入到一个ini文件中
	"""
	config = RawConfigParser()
	config.add_section("info")
	for k, v in d.items():
		config.set("info", k, v)

	with open(filename, "wb") as configfile:
		config.write(configfile)

def listfiles(path):
	"""获取目录中的所有文件
	"""
	files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	full_path_files = [os.path.join(path, f) for f in files]
	return full_path_files

def get_file_name(path):
	"""获取文件名称
	"""
	filename = os.path.split(path)[1]
	return os.path.splitext(filename)[0] + ".ini"

def gen_configs(path):
	files = listfiles(path)
	for file in files:
		d = genconfig(file)
		filename = get_file_name(file)
		print "写入文件：", filename
		write_config(d, os.path.join("../casks", filename))

if __name__ == "__main__":
	gen_configs("../../homebrew-casks/")
