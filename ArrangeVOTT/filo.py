# ------概要------
# このファイルは、VoTTで出力された(train.txt,test.txt等の)テキストファイルの中身の順序を適切に並べるコード。
# VoTTで作成されたこれらのファイルはパスが適切に指定できてないため作成。
# 改行+横並びで出力される。本来は一行ごとにファイルのパスが必要。
# ------使い方------
# python filo.py <filename>
# filenameは相対パス
# [例]pytohn filo.py train.txt
# -----------------

#!/usr/bin/env python                                                           
#coding:UTF-8
import os
import sys

def chTrainData(fileName):

	f = open(fileName,'r')
	Allf = f.read()
	print("---------print default source---------")
	print Allf
	text = Allf.replace('\n','')
	print("---------print delete return---------")
	print text
	text = text.replace('gd','g\nd')
	print("---------print return finish---------")
	print text
	f.close()

	os.remove(fileName)

	f = open(fileName,'w')
	f.write(text)
	f.close()

if __name__ == '__main__':
	args = sys.argv

	if len(args) == 2:
		name = args[1]
		chTrainData(name)
	else:
		print('以下形式でnameを指定してください')
		print('$ python filo.py <name>')
        quit()
