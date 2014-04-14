#!/usr/bin/python
# -*- coding: utf-8 -*-
from rgb2gali import *
from gali2rgb import *

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Converts RGB to Galillibob and vice versa.')
	parser.add_argument('inputType', help='What type of input are you providing? Options: rgb, gali', type=str)
	parser.add_argument('color', help='Color to convert.', type=str)
	try:
		args = parser.parse_args()
	except Exception as e:
		print e
		sys.exit(1)

	if args.inputType == 'rgb':
		convertRGBToGali(args.color)
	else:
		convertGaliToRGB(args.color)
