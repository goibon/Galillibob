#!/usr/bin/python
# -*- coding: utf-8 -*-
from common import *
import argparse

def convertRGBToGali(colorRGB):
	print colorRGB[0:2] + " | " + colorRGB[2:3] + " | " + colorRGB[3:5] + " | " + colorRGB[5:6] + " | " + colorRGB[6:8] + " | " + colorRGB[8:9]
	print beginnings[int(colorRGB[0:2])] + middles[int(colorRGB[2:3])] + middles[int(colorRGB[3:5]) ] + middles[int(colorRGB[5:6])] + middles[int(colorRGB[6:8])] + endings[int(colorRGB[8:9])]
