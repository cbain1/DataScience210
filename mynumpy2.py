import sys
import random 
import re
import numpy as np
from skimage import io
import matplotlib.pyplot as plt



def main():

	photo = io.imread('cheetah-leaping.jpg')
	print(photo.shape)
	plt.imshow(photo)
	plt.show()
	


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()