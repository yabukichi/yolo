#!/usr/bin/env python                                                           
#coding:UTF-8
# ----------------
# python2系
# はじめに、yamada01等があるフォルダと同じ階層に配置すること。
# [例]
# car_data
#  - yamada01
#    - data
#    - yolo.cfg
#  - yamada02
#  - yamada03
#  - ...
#  - ..
#  - .
#  rebuild.py 

import os
import re
import sys
import glob
import shutil
 
#os.rename('twt.txt','miffy1.txt')

# 配列を用意する。この配列はもとファイルのmaxnumberを用意するためのもの。関数外(というかglobal)に設置しているのはどこからでも参照できるようにするため。
numlist = []

def fileMaxNumber(fname) :
	i = 0

	files=glob.glob(fname + "/data/obj/*.jpg") 

	for file in files:
		# print(file)
		maxnum = re.sub(r'\D', '', files[i]) #数字を抽出する。([例]0319028)
		adnum = re.sub(r'\d{6}', '', maxnum) #maxnumから余分な数字を排除する。([例]8)
		# print(maxnum)
		adnum = int(adnum)
		numlist.append(adnum)
		i += 1
		# print(i)

	# print(numlist)
	numlist.sort(reverse = True)
	# print(numlist)
	# print(type(numlist[2]))
	# print(numlist[0])

def fileChanger(dfname,chname,chtxt,dftxt) :
	x = numlist[0] + 1
	newjpg = []

	test_data = open(chtxt, "r")
	# chjpgfile = chname + "/data/obj/"
	# Alltest = test_data.read()
	# print Alltest

	# 一行ずつ読み込んでは表示する

	for line in test_data:
		print line
		line = line.strip()
		print chname + "/" + line
		print chname + "/data/obj/car_movie_frame_" + str(x) + ".jpg"
		print x
		newjpg.append("data/obj/car_movie_frame_" + str(x) + ".jpg\n")

		os.rename(chname + "/" + line, chname + "/data/obj/car_movie_frame_" + str(x) + ".jpg")
		# テキストファイルの中身の数値を変更
		reline = line.replace(".jpg",".txt")
		print reline
		os.rename(chname + "/" + reline, chname + "/data/obj/car_movie_frame_" + str(x) + ".txt")
		shutil.copyfile(chname + "/data/obj/car_movie_frame_" + str(x) + ".txt", dfname + "/data/obj/car_movie_frame_" + str(x) + ".txt")
		shutil.copyfile(chname + "/data/obj/car_movie_frame_" + str(x) + ".jpg", dfname + "/data/obj/car_movie_frame_" + str(x) + ".jpg")

		x += 1
	# ファイルをクローズする
	test_data.close()

	print newjpg

	# ファイル名を変更したものを作成。
	os.remove(chtxt)

	newtrainfile = open(chtxt,"a")
	newtrainfile.writelines(newjpg)
	newtrainfile.close()

	chfile = open(chtxt,"r")
	chf = chfile.read()
	chfile.close()

	dffile = open(dftxt,"r")
	dff = dffile.read()
	dffile.close()

	alltextfile = dff + chf
	alltextfile = alltextfile.replace('gd','g\nd')
	os.remove(dftxt)

	filechange = open(dftxt,"w")
	filechange.write(alltextfile)
	filechange.close()


def changeTxt(dataTxt):
	# trainTxt = chname + "/data/train.txt"
	# txtをyoloで使用可能な形式に変換する
	f = open(dataTxt,'r')
	Allf = f.read()
	print "---------print default source---------" + "\n"
	print Allf + "\n"
	text = Allf.replace('\n','')
	# print "---------print delete return---------"
	# print text
	text = text.replace('gd','g\nd')
	print "---------print return finish---------" + "\n"
	print text + "\n"
	f.close()

	os.remove(dataTxt)

	f = open(dataTxt,'w')
	f.write(text)
	f.close()

if __name__ == '__main__':
	args = sys.argv

	if len(args) == 3:
		dfaultname = args[1]
		dftestTxt = dfaultname + "/data/test.txt"
		dftrainTxt = dfaultname + "/data/train.txt"
		changename = args[2]
		chtestTxt = changename + "/data/test.txt"
		chtrainTxt = changename + "/data/train.txt"
		fileMaxNumber(dfaultname)

		print "\n" + str(numlist[0] + 1) + "\n"

		changeTxt(dftestTxt)
		changeTxt(dftrainTxt)
		changeTxt(chtestTxt)
		changeTxt(chtrainTxt)		
		fileChanger(dfaultname,changename,chtrainTxt,dftrainTxt) #changeTxtで全てのテキストファイルの名前を変更した後じゃないとファイルがおかしくなるので注意。
		fileMaxNumber(dfaultname) #trainファイルを転送後にもう一度最大値の計算をさせる
		fileChanger(dfaultname,changename,chtestTxt,dftestTxt) #changeTxtで全てのテキストファイルの名前を変更した後じゃないとファイルがおかしくなるので注意。

	else:
		print '以下形式でフォルダを指定してください'
		print '$ python rebuild.py <元になるフォルダ> <統合するフォルダ>'
        quit()
	

























