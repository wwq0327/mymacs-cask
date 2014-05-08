#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import zipfile

def extract_zip(zfile, path):
	if not zipfile.is_zipfile(zfile):
		print "%s 不是有效的zip文件，或文件已坏损" % zfile
		sys.exit(0)

	z = zipfile.ZipFile(zfile)
	z.extractall(path)
	print "文件解压到:%s" % path
	z.close()
	
def test():
	extract_zip("../testdatas/test.zip", "/tmp")

if __name__ == '__main__':
	test()
