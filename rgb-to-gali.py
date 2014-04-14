#!/usr/bin/python
# -*- coding: utf-8 -*-
from common import *
import argparse

def convertRGBToGali(colorRGB):
	print beginnings[int(colorRGB[0:2])] + middles[int(colorRGB[2:3])] + middles[int(colorRGB[3:5]) ] + middles[int(colorRGB[5:6])] + middles[int(colorRGB[6:8])] + endings[int(colorRGB[8:9])]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Converts RGB to Galillibob and vice versa.')
	parser.add_argument('color', help='RGB color to convert to Galillibob.', type=str)
	try:
		args = parser.parse_args()
	except Exception as e:
		print e
		sys.exit(1)
	convertRGBToGali(args.color)