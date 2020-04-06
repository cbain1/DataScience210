import sys
import random 
import re

def main():
	file = open("genome.html").read()

	numOpen = {}
	numClose = {}
	badTags = 0

	openTags = re.finditer(r'\<(\w+)\s*[^>]*\>', file) 
	for tag in openTags:
		name = tag.group(1).lower()
		if name in numOpen:
			numOpen[name]+=1
		else:
			numOpen[name]=1
	closeTags = re.finditer(r'\<[/](\w+)\s*[^>]*\>', file)
	for tag in closeTags:
		name = tag.group(1).lower()
		if name in numClose:
			numClose[name]+=1
		else:
			numClose[name]=1
	
	print("\nHTML Tag Information for the file genome.html\n",file=)
	print("Tag\t\tNumber Opened\t\tNumber Closed")
	for key in numOpen:
		if key not in numClose:
			numClose[key] = 0
		if numOpen[key] > numClose[key] and numClose[key]>0:
			badTags+=numOpen[key]-numClose[key]
		print("{}\t\t".format(key),"{}".format(numOpen[key]),"\t\t\t\t{}".format(numClose[key]))
	print("-"*50)
	print("Total \"Bad\" Tags\t\t\t\t",badTags)
	

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()