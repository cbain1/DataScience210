import sys
import random 
import re
import math
import numpy as np
from skimage import io
import matplotlib.pyplot as plt




def main():
	
	photo = io.imread('cheetah-leaping.jpg')
	# looks like two dim array, each square is a pixel represented with an RBG code (3 dim array) - numbers are 0-255 255=2^8-1
	# 0 is black, brightest red is 255
	print(photo.shape)
	plt.imshow(photo)
	plt.show()
	
	'''
	# show every other row 
	plt.imshow(photo[::2])
	plt.show() #this basically just stretches the cheetah horizontally 

	# shrink image by half 
	plt.imshow(photo[::2,::2])
	plt.show()

	# print the cheetah upside down 
	plt.imshow(photo[::-1])
	plt.show()

	# print upside down and backwards 
	# plt.imshow(photo[::-1,::-1])
	# plt.show()

	# print just the head 
	plt.imshow(photo[60:125,:75])
	plt.show()

	# fuck with the cheetah 

	# for x in range(324):
	# 	for y in range(470):
	# 		for rgb in range(3):
	# 			photo[x][y][rgb] = math.sin(photo[x][y][rgb])
	# plt.imshow(photo)
	
	# photo_sin = np.sin(photo) #this does take the sign but it wont print it bc its terrible
	# plt.imshow(photo_sin)
	# plt.show()

	print(np.sum(photo)) #sum of photo
	print(np.prod(photo)) #product of photo
	print(np.mean(photo))
	print(np.std(photo))
	print(np.var(photo))
	print(np.min(photo))
	print(np.max(photo))
	print(np.argmin(photo)) #where in the photo does the min exist (x*y*3)+y*3+z
	print(np.argmax(photo)) #where in the photo does the max exist


	identityMatrix = np.identity(7)
	print(identityMatrix) #1's in left to right downward diagonal, 0's in everything else 

	sample = np.array(identityMatrix.diagonal()) #gives all diagonals in a list
	print(sample)

	poly = np.poly([-1,1,1,10]) #finds polynomial that coencides with these roots
	print(poly)

	roots = np.roots([1,4,-2,3]) #finds root for a given polynomial
	print(roots)

	# scipy is also a thing that exists and does lots of things -- you can see the things through help(scipy)


	# more stuff to know about numpy
	# 1) conditions apply to the entire array so you dont have to loop through the things manually 
	z = np.array([1,2,3,4,5])
	print(z<3) #will give you a list of booleans given the condition

	# also numpy arrays support array masking 
	r = z[z<3]
	print(r)

	# lets use array masking to produce a different version of the cheetah
	# where executes this thing on each element of photo 
		# if photo>100 photo becomes 255, else photo becomes 0
	photoMasked = np.where(photo>100,255,0) #anything that is satisfied by the condition is replaced with 0
	plt.imshow(photoMasked)
	plt.show() #rave cheetah

	'''


	a = np.array([1,2,3,4,5])
	b = np.array([6,7,8,9,0])

	print(a+b)
	print(a*b)
	print(a+30)
	print(a@b) #dot product

	#now we will see if we can manipulate sin
	photo_sin = np.sin(photo) #list of -1 to 1
	photo_sin += 1
	photo_sin *= 127 #now numbers range of 0 to 254 

	photo_sin = np.uint8(photo_sin)

	print(type(photo_sin[0][0][0]))

	# print the sin of cheetah 
	plt.imshow(photo_sin)
	plt.show() #cheetah trip

	ct = photo_sin
	ct = ct/127
	ct = ct - 1
	ct = np.arcsin(ct)
	ct = np.uint8(ct) #this is the line that fucks us 

	plt.imshow(ct)
	plt.show()

	plt.imshow(photo[:,:,0].T)
	plt.show()



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()