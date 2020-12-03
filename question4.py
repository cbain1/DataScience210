import sys
import random 
import re
import math



def findIPs(file, ipAddresses, computerTypes, count): 
	for line in file: 
		count+=1
		ip = line.split()[0]
		if ip in ipAddresses: 
			ipAddresses[ip] +=1
		else: 
			ipAddresses[ip] = 1
		userAgent = line.split('"')[-2]
		if "Windows" in userAgent: 
			computer= "Windows"
		elif "Macintosh" in userAgent:
			computer =  "Macintosh"
		elif "iPhone" in userAgent:
			computer =  "iPhone"
		elif "Android" in userAgent:
			computer = "Android"
		else:
			items = re.findall(r'(\w+bot|bot\.htm|spider| \w+Bot | Spider | Crawler|crawler)', userAgent)
			if len(items) == 0: 
				computer = "Other/Unknown"
			else: 
				computer = "Spider/Bot"
		if computer in computerTypes: 
			computerTypes[computer] +=1
		else: 
			computerTypes[computer] = 1


	return count

def main():

	ipAddresses = {}
	computerTypes = {}
	count = 0
	file = open("access_log.txt")
	count = findIPs(file, ipAddresses, computerTypes, count)

	# part 1
	print("Part 1: ")
	print("Total access calls: ",count, "\n")

	# part 2
	print("Part 2: ")
	print("%-20s %s" %("IP Address", "Number of Calls Made"))
	for key in ipAddresses:
		print("%-20s %s" %(key, ipAddresses[key]))

	print()

	print("Part 3: ")
	print("%-20s %s" %("Computer Type", "Number of Calls Made"))
	# part 3 
	for key in computerTypes:
		print("%-20s %s" %(key, computerTypes[key]))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()