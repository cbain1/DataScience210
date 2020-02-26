import sys
import random 
import re

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def findStuff(babyFile, relevantInfo):
	#finding patterns
	info = re.finditer(r'<td>(\d*)</td><td>([A-Z]\w*)</td><td>([A-Z]\w*)',babyFile)
	for line in info:
		relevantInfo[(line.group(2),'Male')] = line.group(1)
		relevantInfo[(line.group(3),'Female')] = line.group(1)
	return relevantInfo

def main():

	#File setup
	eprint("What is the name of the baby file you would like to examine? ")
	fileRequest = input()
	babyFile = open(fileRequest).read()

	year = re.findall(r'\d{4}',fileRequest)
	#heading the table
	print('Most Popular Baby Names for', year[0])
	print('\nGender\t\tName\t\tRank')

	relevantInfo = {}
	#Where the names will go 
	findStuff(babyFile, relevantInfo)
	
	# printing and sorting
	for key in sorted(relevantInfo.keys()):
		if len(key[0]) > 7:
			print(key[1]+'\t\t'+key[0]+'\t'+relevantInfo[key])
		elif len(key[0])<4:
			print(key[1]+'\t\t'+key[0]+'\t\t\t'+relevantInfo[key])
		else: 
			print(key[1]+'\t\t'+key[0]+'\t\t'+relevantInfo[key])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()