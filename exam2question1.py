import sys
import random 
import re
import math
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import imageio

def main():
	
	photo = io.imread('gandalf.jpg')
	array = np.array(photo)

	nored=photo.copy()
	nored[nored[:,:,0]>0,0]=0

	blue= nored.copy()
	green = nored.copy()

	blue[blue[:,:,1]>0,1]=0
	plt.imshow(blue)
	plt.show()
	imageio.imwrite('bluemask.jpg',blue)

	green[green[:,:,2]>0,2]=0
	plt.imshow(green)
	plt.show()
	imageio.imwrite('greenmask.jpg',green)

	nogreen=photo.copy()
	nogreen[nogreen[:,:,1]>0,1]=0
	red=nogreen
	red[red[:,:,2]>0,2]=0
	plt.imshow(red)
	plt.show()
	imageio.imwrite('redmask.jpg',red)



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()