def rgb2hex(color):
	return hex(int(color[0:3])).lstrip("0x") + hex(int(color[3:6])).lstrip("0x") + hex(int(color[6:9])).lstrip("0x")