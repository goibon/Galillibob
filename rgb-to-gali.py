#!/usr/bin/python
# -*- coding: utf-8 -*-
beginnings = ['Gall', 'Sim', 'Kasp', 'Rasm', 'Christ', 'Kats', 'Mar', 'Benj', 'Sø', 'Jac', 'Johns', 'Denn', 'Alex', 'Jens', 'Worms', 'Mich', 'Ant', 'Majk', 'Asg', 'Po', 'Mikk', 'Cam', 'Ol', 'Uld', 'Andr']

middles = ['ill', 'ib', 'ob', 'on', 'of', 'u', 'a', 'ren', 'and', 'i', 'ist', 'ah', 'e', 'esg', 'len', 'erg', 'ulb', 'ul', 'bell', 'el', 'in', 'iss', 'ori', 'ab', 'ol']

endings = ['us', 'fer', 'aki', 'ia', 'in']

colorRGB = raw_input("Enter color in RGB (e.g. 255255255): ")

print beginnings[int(colorRGB[0:2]) - 1] + middles[int(colorRGB[2:3]) - 1] + middles[int(colorRGB[3:5]) - 1] + middles[int(colorRGB[5:6]) - 1] + middles[int(colorRGB[6:8]) - 1] + endings[int(colorRGB[8:9]) - 1]
