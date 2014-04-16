import os
import webbrowser

def displayColorInNewTab(color):
	hexColor = hex(int(color[0:3])).lstrip("0x") + hex(int(color[3:6])).lstrip("0x") + hex(int(color[6:9])).lstrip("0x")
	f = open('color.html','w')
	message = """<html>
	<body bgcolor="#%s"></body>
	</html>""" %hexColor
	f.write(message)
	f.close()

	filePath = os.path.join(os.path.dirname(__file__), 'color.html')
	webbrowser.open_new_tab('File://'+filePath)