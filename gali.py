#!/usr/bin/python
# -*- coding: utf-8 -*-
from rgb2gali import *
from gali2rgb import *
import argparse
import webbrowser
import os
from colordisplay import displayRGBColorInNewTab
from rgb2hex import rgb2hex

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Converts RGB to Galillibob and vice versa.')
	parser.add_argument('inputType', help='What type of input are you providing? Options: rgb, gali', type=str)
	parser.add_argument('color', help='Color to convert.', type=str)
	parser.add_argument('-b', '--browser', help='Display the color in a browser.', action='store_true')
	parser.add_argument('-p', help='Prints the result of the conversion in the terminal.', action='store_true')

	try:
		args = parser.parse_args()
	except Exception as e:
		print e
		sys.exit(1)
	
	color = None
	if args.inputType == 'rgb':
		hexColor = rgb2hex(args.color)
		color = convertRGBToGali(args.color)
	else:
		color = convertGaliToRGB(args.color)
		hexColor = rgb2hex(color)
	if args.p:
		print color
	if args.browser:
		displayRGBColorInNewTab(hexColor)