#!/usr/bin/python
# -*- coding: utf-8 -*-
from rgb2gali import *
from gali2rgb import *
import argparse
import webbrowser
import os
from colordisplay import displayRGBColorInNewTab
from rgb2hex import *
from unittests import runtests



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Converts RGB to Galillibob and vice versa.')
	parser.add_argument('inputType', help='What type of input are you providing? Options: rgb, gali', type=str)
	parser.add_argument('color', help='Color to convert.', type=str)
	parser.add_argument('-b', '--browser', help='Display the color in a browser.', action='store_true')
	parser.add_argument('-p', help='Prints the result of the conversion in the terminal.', action='store_true')
	parser.add_argument('-t', '--test', help='Runs unit tests.', action='store_true')

	try:
		args = parser.parse_args()
	except Exception as e:
		print e
		sys.exit(1)

	if args.test:
		runtests()

	
	if args.inputType == 'rgb':
		rgb = splitDecRGB(args.color)
		gali = convertRGBToGali(rgb)
	else:
		gali = args.color
		rgb = splitDecRGB(convertGaliToRGB(args.color))

	if args.p:
		print "rgb: %s" %rgb
		print "gali: " + gali 
	if args.browser:
		displayRGBColorInNewTab(rgb, gali)