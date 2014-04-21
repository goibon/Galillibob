from rgb2gali import *
from gali2rgb import *
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

def runtests():
	suite = unittest.TestLoader().loadTestsFromTestCase(ColorTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)