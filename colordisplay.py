import os
import webbrowser

def displayRGBColorInNewTab(color):
	f = open('color.html','w')
	message = """<html>
	<body bgcolor="#%s"></body>
	</html>""" %color
	f.write(message)
	f.close()

	filePath = os.path.join(os.path.dirname(__file__), 'color.html')
	webbrowser.open_new_tab('File://'+filePath)