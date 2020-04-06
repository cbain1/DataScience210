import sys
import random 
import re
import operator
import math
import numpy as np
from poofQ1 import *

def main():
	allYearRelevantInfo = {}
	scores = {}
	# make dictionary 
	for x in range(1990,2010,2):
		yearFile = open("baby{}.html".format(x)).read()
		allYearRelevantInfo[x] = {}
		findStuff(yearFile, allYearRelevantInfo[x])



	#Justification for Our Scoring: 
		'''
		We decided to score each place with weighting similar to how each place in Mario Kart is scored. We thought this was best because it easily accounts for variation across years including when a name drops off the list all together. We decided to cut it off at 20 because that was double the number of names we wanted to output at the end. 

		Within that top 20, we broke down the difference between each ranking by different point values. For example, the difference between first and second place is 25, but the difference between fourth and fifth is 10 points. 

		We then determined that our pattern fit a function in terms of ln(x). Specifically, we found y = -50ln(x) + 161. We then chose to calculate scores based on this equation. 

		For example, if Abe receives first place in one year and 10th place in the following year, he will receive a score of roughly 207 and Kevin who receives 5th in both years, will receive a total score of roughly 160. 

		A second example shows you a more extreme example. If Abe receives first in one year and 100 in the following year, he will receive a total score of 31 while Kevin who receives rank 50 in one year and 51 in the following year, he would receive a total score of -69. 

		'''
	for key in allYearRelevantInfo: #key is year 
		for x in allYearRelevantInfo[key]:
			if x not in scores:
				scores[x] = (-1*np.log(int(allYearRelevantInfo[key][x]))+161)
			else:
				scores[x]+=(-1*np.log(int(allYearRelevantInfo[key][x]))+161)
				
	print(scores)


	sorted_names = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)


	print("Top 10 Male Names Across All Years")
	count = 1
	place = 0
	while count < 11 and place<len(sorted_names):
		if sorted_names[place][0][1] == 'Male':
			print(count,'\t\t',sorted_names[place][0][0])
			count+=1
		place+=1
	print()
	print("Top 10 Female Names Acorss All Years")
	count = 1
	place = 0
	while count < 11 and place<len(sorted_names):
		if sorted_names[place][0][1] == 'Female':
			print(count,'\t\t',sorted_names[place][0][0])
			count+=1
		place+=1
	print()
	print("Top 10 Names of All Years, Regardless of Gender")
	count = 1
	place = 0
	while count < 11 and place<len(sorted_names):
		print(count,'\t\t',sorted_names[place][0][0])
		count+=1
		place+=1

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()