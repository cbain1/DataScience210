# Savannah Spears
import sys
import random
import re

def findStuff(file, links, i, count):

	linklist = re.findall(r'(:|=)"*((http:|https:)*(/{1,2})[^\"{}<>\(\)]+)("|\s)', file)

	for link in linklist:
		fullLink= link[1]
		fileID = i

		a = link[4]

		b = a.split("/")[0]
		if "." in b:
			do = b.split(".")[-1]
			domain = do.split("\"")[0]
		else:
			domain = ""
		
		c = a.split("/")[-1]
		if "." in c:
			d = c.split(".")[-1]
			linkType = d.split("\"")[0]
		else:
			linkType = ""
		
		if link[2] == "http:" or link[2] == "https:" or link[3] == "//":
			explicit = 1
		else:
			explicit = 0

		links[count] = (fileID,fullLink,linkType,domain,explicit)
		count += 1
	return count

def main():

	links = {}
	count=1
	for i in range(1,201):
		file = open("file{}.html".format(i)).read()
		count = findStuff(file, links, i, count)

	outputFile = open("savannah.csv",'w')
	print("linkID,fileID,link,linkType,domain,explicit", file=outputFile)
	for key in links:
		print("{}".format(key)+","+"{}".format(links[key][0])+","+"\"{}\"".format(links[key][1])+","+"{}".format(links[key][2])+","+"{}".format(links[key][3])+","+"{}".format(links[key][4]) ,file=outputFile)


if __name__ == '__main__':
    main()