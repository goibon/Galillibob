#!/usr/bin/python
# -*- coding: utf-8 -*-
from rgb2gali import *
from gali2rgb import *
import argparse
import webbrowser
import os
from colordisplay import displayRGBColorInNewTab
from rgb2hex import *
import unittest

class ColorTestCase(unittest.TestCase):
	def setUp(self):
		self.rgbcolor = splitDecRGB('255255255')
		self.galicolor = 'hajrarbhlarbhlydn'

	def tearDown(self):
		# self.widget.dispose()
		self.rgbcolor = None
		self.galicolor = None
        
	def test_rgb_to_gali(self):
		rgblist = [0,0,0]
		for x in xrange(0,256):
			rgblist[0] = x
			for y in xrange(0,256):
				rgblist[1] = y
				for z in xrange(0,256):
					rgblist[2] = z
					gali = convertRGBToGali(rgblist)
					rgb = addZeros(str(rgblist[0]),3) + addZeros(str(rgblist[1]),3) + addZeros(str(rgblist[2]),3)
					self.assertEqual(rgb, convertGaliToRGB(gali)) 

	def check_rgb_gali(red, green, blue):
		initialRGB = []
		initialRGB.append(red)
		initialRGB.append(green)
		initialRGB.append(blue)
		initialRGB = splitDecRGB(rgb)

		gali = convertRGBToGali(initialRGB)
		rgb = convertGaliToRGB(gali)

		self.assertEqual(gali, rgb)
	# def test_default_size(self):
	# 	self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')
	

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
		suite = unittest.TestLoader().loadTestsFromTestCase(ColorTestCase)
		unittest.TextTestRunner(verbosity=2).run(suite)

	
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