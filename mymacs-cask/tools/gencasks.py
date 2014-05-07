#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''读取.rb文件，生成python可读到的ini文件
'''
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

	d = {
		"url": url,
		"homepage": homepage,
		"version": version,
		"link": link}
	
	return d

def write_config(d):
	"""将信息写入到一个ini文件中
	"""
	config = RawConfigParser()
	config.add_section("info")
	for k, v in d.items():
		config.set("info", k, v)

	with open("exp.ini", "wb") as configfile:
		config.write(configfile)
	
def test():
	d = genconfig("../../testdatas/yubiswitch.rb")
	print d
	write_config(d)
	
if __name__ == "__main__":
	test()
