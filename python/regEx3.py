import sys
import random 
import re
#import regex -- strict supersset of re

# Define a main() function that prints a little greeting.
def main():

    names = '''
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''

    #Ex. 1 - Print out only males 
    males = re.findall(r'Mr\.?\s\w{1,7}',names)
    print(males)
    print()

    #Could also be done like this
    males = re.findall(r'Mr[.\s]+\w*',names)
    print(males)

    fhand = open('regexdata.txt')
    file = fhand.read()
    # print(file)

    #Print all the phone numbers from this file 
    phones = re.findall(r'\d{3}[-]\d{3}[-]\d{4}',file)
    # print(phones)
    print(len(phones))
    fhand.close()

    fhand = open('regexdata.txt')
    file = fhand.read()
    #report the number of people who live in each zipcode
    zipcodes = re.findall(r'\d{5}\n',file)

    zipCount = {}
    for elem in zipcodes:
        if elem in zipCount: 
            zipCount[elem]+=1
        else:
            zipCount[elem]=1
    # print(zipCount)
    print(len(zipCount))
    fhand.close()
    
    # now we will learn a group 
    # it encloses the part of the search you actually care about 
    fhand = open('regexdata.txt')
    file = fhand.read()
    #report the number of people who live in each zipcode
    zipcodes = re.findall(r'(\w\w)\s(\d{5})\n',file)
    # since i put the thing in perentheses above, it only returns this part instead of the rest of it instead of returning the whole thing 

    zipCount = {}
    for elem in zipcodes:
        if elem in zipCount: 
            zipCount[elem]+=1
        else:
            zipCount[elem]=1
    # print(zipCount)
    print(zipCount)
    fhand.close()
    print()
    print()




    #now match objects 
    fhand = open('regexdata.txt')
    contents = fhand.read()
    regionInfo = re.finditer(r'(\w\w)\s(\d{5})\n', contents)
    for instance in regionInfo:
        print(instance.group(0)) # this does the whole thing but not in a match object

# Look again, now we shall see how often each state appears 
    fhand = open('regexdata.txt')
    contents = fhand.read()
    states = {}
    regionInfo = re.finditer(r'(\w\w)\s(\d{5})\n', contents)
    for instance in regionInfo:
        if instance.group(1) not in states:
            states[instance.group(1)] = 1
        else:
            states[instance.group(1)] +=1
    print(states)
    fhand.close()


# Now only WI and IN
    fhand = open('regexdata.txt')
    contents = fhand.read()
    states = {}
    regionInfo = re.finditer(r'(IN|VA)', contents) #this now matches only IN or WI
    for instance in regionInfo:
        print(instance)
    fhand.close()


# Now only zipcodes for those states
    fhand = open('regexdata.txt')
    contents = fhand.read()
    states = {}
    regionInfo = re.finditer(r'(IN|VA)\s(\d{5})', contents) #this now matches only IN or WI
    for instance in regionInfo:
        print(instance.group(2))
    fhand.close()

# Now only Arnolds as last names
    fhand = open('regexdata.txt')
    contents = fhand.read()
    firstName = re.finditer(r'(\w+)\sArnold',contents)
    for names in firstName:
        print(names.group(1))
    fhand.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()