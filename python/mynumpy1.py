import sys
import random 
import re
import numpy as np



def main():
	# Create our first ndarray
	a = np.zeros(5)
	print(a)

	print(type(a))
	print(type(a[0]))

	b = np.ones(10)
	print(b)
	print(b.shape)
	b.shape = (10,1)
	print(b)
	# this builds the shape of the data structure 
	print(b.shape)
	b.shape = (5,2)
	print(b)
	# you cannot reshape an array of a given size into a shape that is a different size

	# create the numbers from 2 to 10, with a total of 6 elements
	z = np.linspace(2,10,6)
	print(z)

	# Convert a python list to an ndarray
	z=np.array([10,20])
	print(z)

	# conversion with a list variable 
	a_list = [1,2,3]
	z = np.array(a_list)
	print(z)

	# what if you have mismatched type -- in this case it converts all of them to strings 
	# num py arrays must all be the same datatype <----- LIES
	a_list = [12,13,'taco']
	z=np.array(a_list)
	print(z)
	print(z[1], type(z[1]))

	# now we do things a little differently 
	b_list = [1,2,[3,'taco']]
	z= np.array(b_list)
	print(z)
	# this gives you just taco 
	print(z[2][1])
	# here you can see that the array contains a list and that is cool with numpy 
	# this list can have as many datatypes as possible 


	# lets create an actual 2dim array from a 2dim python list that is regular aka a full matrix 
	c_list = [[1,2,3],[4,5,6]]
	z = np.array(c_list)
	print(z)
	# if the lists are not the same size, you will get a 1dim array not a 2dim array 
	print(z.shape)


	# create a random numpy array (really a ndarray) 
	np.random.seed()
	zrandomarray = np.random.randint(10,size=6)
	print(zrandomarray)
	# so if i dont set a seed, what does it pick though? the millisecond digit of the time at which you ran the thing

	# nd arrays can in fact be sliced 
	print(zrandomarray[0:2])
	print(zrandomarray[-1])

	


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()