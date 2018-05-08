import os
import datetime

def move(member):

	now = str(datetime.datetime.now())
	src = '[directory name/image file]'
	des = member + '/' + now + '.jpg'

	os.rename(src,des) # change the image file name and directory
