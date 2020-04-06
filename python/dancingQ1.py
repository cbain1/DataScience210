import sys
import random 
import re

def findStuff(file, links, fileNum,count):

	info = re.finditer(r'(=|,|:\s|:|[()]){1}(\'|")?[^;](((http:|https:)?\/{1,2}[^\/\"\'\\\s>]+)([^\'\"\s>]+))',file)

	# group1(quotes or nah), group2(the link through the end), group3(link through the domain), group4(http: or https: or none), group5(eveything after the domain)

	# dictionary: key=id, value(fileNumber, link,linkType,domain,Boolean explicit)
	for match in info:
		if match.group(0)[-1]==".":
			continue
		if "\\" in match.group(3): 
			continue
		domain = ""
		linkType = ""
		remainder = match.group(6).split("/")[-1]
		findType = re.finditer(r'(\.|=)([a-z]{2,4})(\?|$|%)',remainder)
		for stuff in findType:
			linkType = "."+(stuff.group(2)).lower()

		link = match.group(4)
		if "." in link:
			d = "."+link.split(".")[-1]
			domaingroup = re.finditer(r'\.com|\.org|\.net|\.int|\.edu|\.gov|\.mil|\.link|\.a[cdefgilmoqrstuwxz]|\.b[abdefghijmnorstwyz]|\.c[acdfghiklmnoruvwxyz]|\.d[ejkmoz]|\.e[egrstu]|\.f[ijkmor]|\.g[adefghilmnpqrstuwy]|\.h[kmnrtu]|\.i[delmnoqrst]|\.j[emop]|\.k[eghimnprwyz]|\.l[abcikrstuvy]|\.m[acdeghklmnopqrstuvwxyz]|\.n[acefgilopruz]|\.om|\.p[aefghklmnrstwy]|\.qa|\.r[eosuw]|\.s[abcdeghiklmnorstuvxyz]|\.t[cdfghjklmnortvwz]|\.u[agksyz]|\.v[aceginu]|\.w[fs]|\.y[et]|\.z[amw]',d)
			for stuff in domaingroup:
				domain=stuff.group(0)
		if(match.group(5)=="http:" or match.group(5)=="https:"):
			links[count] = (fileNum,match.group(3),linkType,domain,1) 
		else:
			links[count] = (fileNum,match.group(3),linkType,domain,0) 
		count+=1
	return count



def main():

	links = {}
	count=1
	for x in range(1,201):
		file = open("file{}.html".format(x)).read()
		count = findStuff(file, links, x, count)
	
	outputFile = open("links.csv",'w')
	print("linkID,fileID,link,linkType,domain,explicit", file=outputFile)
	for key in links:
		print("{}".format(key)+","+"{}".format(links[key][0])+","+"\"{}\"".format(links[key][1])+","+"{}".format(links[key][2])+","+"{}".format(links[key][3])+","+"{}".format(links[key][4]) ,file=outputFile)

	outputFile.close()


	

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()