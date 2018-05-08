import os

def check():

	visit = False
	path = '[directory path]'
	fileList = os.listdir(path)

	for items in fileList:
		if items.find('image file name') is not -1:
			visit = True
	
	return visit
