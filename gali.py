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
from multiprocessing import Process

class ColorTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_rgb_to_gali_async(self):
		self.loopX()

	def loopX(self):
		for x in xrange(0,256):
			yp = Process(target=self.loopY, args=(x,))
			yp.start()
		yp.join()

	def loopY(self, x):
		for y in xrange(0,256):
			self.loopZ(x,y)

	def loopZ(self, x,y):
		for z in xrange(0,256):
			self.check_rgb_gali(x,y,z)

	def check_rgb_gali(self, red, green, blue):
		initialRGB = [red,green,blue]

		gali = convertRGBToGali(initialRGB)
		rgb = convertGaliToRGB(gali)

		initialRGBZeroed = addZeros(str(initialRGB[0]),3) + addZeros(str(initialRGB[1]),3) + addZeros(str(initialRGB[2]),3)

		self.assertEqual(initialRGBZeroed, rgb)

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