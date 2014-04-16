import os
import webbrowser
from rgb2hex import rgb2hex

def averageColor(rgb):
	average = (rgb[0] + rgb[1] + rgb[2]) / 3
	return average

def displayRGBColorInNewTab(rgb, gali):
	backgroundColor = rgb2hex(rgb[0],rgb[1],rgb[2])
	textColor = 'FFFFFF' if averageColor(rgb) <= 127 else '000000'
	f = open('color.html','w')
	message = """<html>
	<body bgcolor="#%s">
	<div style="font-size:90pt;color:#%s;text-align:center;">%s</div>
	</body>
	</html>""" %(backgroundColor, textColor, gali)
	f.write(message)
	f.close()

	filePath = os.path.join(os.path.dirname(__file__), 'color.html')
	webbrowser.open_new_tab('File://'+filePath)