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
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()