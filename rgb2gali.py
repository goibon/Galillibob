#!/usr/bin/python
# -*- coding: utf-8 -*-
from common import *

def convertRGBToGali(colorRGB):
	#Old rgb2gali method saved, because it would be easier to memorize and do manually.
	#return beginnings[int(colorRGB[0:2])] + middles[int(colorRGB[2:3])] + middles[int(colorRGB[3:5]) ] + middles[int(colorRGB[5:6])] + middles[int(colorRGB[6:8])] + endings[int(colorRGB[8:9])]

	R = int(colorRGB[0:3])
	G = int(colorRGB[3:6])
	B = int(colorRGB[6:9])
	#print "RGB: " + str(R) + ":" + str(G) + ":" + str(B)

	calc = (R * 256**2) + (G * 256) + (B)
	#print "calc = " + str(calc)

	a = calc / 64**3
	#print "a = " + str(a)
	calc -= a * 64**3
	#print "calc = " + str(calc)
	b = calc / 64**2
	#print "b = "+ str(b)
	calc -= b * 64**2
	#print "calc = " + str(calc)
	c = calc / 64
	#print "c = " + str(c)
	calc -= c * 64
	#print "calc = " + str(calc)
	d = calc
	#print "d = " + str(d)

	#print str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d)

	return beginnings[a] + middles[b] + middles[c] + endings[d]
