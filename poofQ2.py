import sys
import random 
import re
from poofQ1 import *

def main():
	relevantInfo = {}
	allYearRelevantInfo = {}

	# make dictionary 
	for x in range(1990,1994,2):
		yearFile = open("baby{}.html".format(x)).read()
		allYearRelevantInfo[x]= findStuff(yearFile, 	relevantInfo)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()