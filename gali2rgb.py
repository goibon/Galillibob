#!/usr/bin/python
# -*- coding: utf-8 -*-
from common import *
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def addZeros(theSeg, amount):
   zeroedSeg = ""
   for i in range(0, amount - len(theSeg)):
      zeroedSeg += "0"
   zeroedSeg += theSeg
   return zeroedSeg

def convertGaliToRGB(colorGali):
	for vowel in vowels:
	   colorGali = colorGali.replace(vowel, "|" + vowel)

	firstVocal = colorGali.find("|")
	colorGali = colorGali[0:firstVocal] + colorGali[firstVocal + 1:]
	arrGali = colorGali.split("|")

	galiCode = ""
	segNum = 0
	isShort = 1
	for galiSegment in arrGali:
	  if segNum == 0:
	     galiCode += str(addZeros(str(beginnings.index(galiSegment)), 2))
	  elif segNum < len(arrGali) - 1:
	     if isShort == 1:
		galiCode += str(middles.index(galiSegment))
		isShort = 0
	     else:
		galiCode += str(addZeros(str(middles.index(galiSegment)), 2))
		isShort = 1
	  else:
	     galiCode += str(endings.index(galiSegment))
	  segNum = segNum + 1

	return galiCode
