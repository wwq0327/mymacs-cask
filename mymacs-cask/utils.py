#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import zipfile

## style dict
STYLE = {
	"clear"  : "\033[0m",
	"red"    : "\033[31m",
	"green"  : "\033[32m",
	"yellow" : "\033[33m",
	"blue"   : "\033[34m",
	"purple" : "\033[35m",
	"cyan"   : "\033[36m",
	"white"  : "\033[37m",
	}
	
def extract_zip(zfile, path):
	if not zipfile.is_zipfile(zfile):
		print "%s 不是有效的zip文件，或文件已坏损" % zfile
		sys.exit(0)

	z = zipfile.ZipFile(zfile)
	z.extractall(path)
	print "文件解压到:%s" % path
	z.close()

def highlight(style, text):
	"""打印彩色的终端颜色
	"""
	k = style.lower()
	if k not in STYLE.keys():
		return text
	return ("%("+k+")s" + text + "%(clear)s") % STYLE
	
def test():
	#extract_zip("../testdatas/test.zip", "/tmp")
	for k in STYLE.keys():
		print highlight(k, "hello, world") + " => " + k

if __name__ == '__main__':
	test()
