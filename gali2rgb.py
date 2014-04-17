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
	b = 1
	segNum = 0
	isShort = 1
	calc = 0
	for galiSegment in arrGali:
	  if segNum == 0:
	     calc = (beginnings.index(galiSegment)) * 64**3
	  elif segNum < len(arrGali) - 1:
	     calc += (middles.index(galiSegment)) * 64**(-segNum+3)
	  else:
	     calc += (endings.index(galiSegment))
	  segNum += 1


	R = calc / (256**2)
	calc -= R * 256**2
	G = calc / 256
	calc -= G * 256
	B = calc

	galiCode = addZeros(str(R), 3) + addZeros(str(G), 3) + addZeros(str(B), 3)

	return galiCode
