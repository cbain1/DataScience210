import sys
import random 
import re
import operator
import math
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

		For example, if Abe receives first place in one year and 10th place in the following year, he will receive a score of 205 and Kevin who receives 5th in both years, will receive a total score of 160. 

		A second example shows you a more extreme example. If Abe receives first in one year and 100 in the following year, he will receive a total score of 150 while Kevin who receives rank 50 in one year and 51 in the following year, he would receive a total score of 0. 

		A well fitting line for the method of scoring here is y=-50lnx+155. 
		'''
	for key in allYearRelevantInfo: #key is year 
		for x in allYearRelevantInfo[key]: #x is (name, gender)
			if int(allYearRelevantInfo[key][x]) == 1:
				if x not in scores: 
					scores[x] = 150
				else:
					scores[x] += 150
			elif int(allYearRelevantInfo[key][x]) == 2:
				if x not in scores:
					scores[x] = 125
				else:
					scores[x] += 125
			elif int(allYearRelevantInfo[key][x]) == 3:
				if x not in scores: 
					scores[x] = 105
				else:
					scores[x] += 105
			elif int(allYearRelevantInfo[key][x]) == 4:
				if x not in scores: 
					scores[x] = 90
				else:
					scores[x] += 90
			elif int(allYearRelevantInfo[key][x]) == 5:
				if x not in scores: 
					scores[x] = 80
				else:
					scores[x] += 80
			elif int(allYearRelevantInfo[key][x]) == 6:
				if x not in scores: 
					scores[x] = 75
				else:
					scores[x] += 75
			elif int(allYearRelevantInfo[key][x]) == 7:
				if x not in scores: 
					scores[x] = 70
				else:
					scores[x] += 70
			elif int(allYearRelevantInfo[key][x]) == 8:
				if x not in scores: 
					scores[x] = 65
				else:
					scores[x] += 65
			elif int(allYearRelevantInfo[key][x]) == 9:
				if x not in scores: 
					scores[x] = 60
				else:
					scores[x] += 60
			elif int(allYearRelevantInfo[key][x]) == 10:
				if x not in scores: 
					scores[x] = 55
				else:
					scores[x] += 55
			elif int(allYearRelevantInfo[key][x]) == 11:
				if x not in scores: 
					scores[x] = 30
				else:
					scores[x] += 30
			elif int(allYearRelevantInfo[key][x]) == 12:
				if x not in scores: 
					scores[x] = 27
				else:
					scores[x] += 27
			elif int(allYearRelevantInfo[key][x]) == 13:
				if x not in scores: 
					scores[x] = 24
				else:
					scores[x] += 24
			elif int(allYearRelevantInfo[key][x]) == 14:
				if x not in scores: 
					scores[x] = 21
				else:
					scores[x] += 21
			elif int(allYearRelevantInfo[key][x]) == 15:
				if x not in scores: 
					scores[x] = 18
				else:
					scores[x] += 18
			elif int(allYearRelevantInfo[key][x]) == 16:
				if x not in scores: 
					scores[x] = 5
				else:
					scores[x] += 5
			elif int(allYearRelevantInfo[key][x]) == 17:
				if x not in scores: 
					scores[x] = 4
				else:
					scores[x] += 4
			elif int(allYearRelevantInfo[key][x]) == 18:
				if x not in scores: 
					scores[x] = 3
				else:
					scores[x] += 3
			elif int(allYearRelevantInfo[key][x]) == 19:
				if x not in scores: 
					scores[x] = 2
				else:
					scores[x] += 2
			elif int(allYearRelevantInfo[key][x]) == 20:
				if x not in scores: 
					scores[x] = 1
				else:
					scores[x] += 1
			else:
			 	if x not in scores: 
			 		scores[x] = 0



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