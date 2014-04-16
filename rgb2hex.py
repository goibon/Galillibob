def splitDecRGB(decimalRGB):
	rgb = []
	rgb.append(int(decimalRGB[0:3]))
	rgb.append(int(decimalRGB[3:6]))
	rgb.append(int(decimalRGB[6:9]))
	
	return rgb

def rgb2hex(red, green, blue):
	result = format(red, 'x') + format(green, 'x') + format(blue, 'x')
	return result