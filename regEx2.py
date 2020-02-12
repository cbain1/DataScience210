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

    phone = '''
    321-555-4321
    123.555.1234
    123*555*1234
    800-555-1234
    900-555-1234
    '''

    testThis = re.search('555',phone)
    print(testThis) #this will print a match object - a match object indicates where the thing is, and what the match is 
    # but were going to ignore match objects 

    testThis = re.finditer('555',phone)
    for x in testThis:
        print(x)
    #the above code will print all match objects matched with 555
    print()
    testThis = re.findall('555',phone)
    print(testThis)

    #So, how can we use this findall function to know more?
    knowMore = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',phone)
    print(knowMore)

    # all characters in brackets
    print()
    knowEvenMore = re.findall(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', phone)
    print(knowEvenMore)

    # all characters not in brackets
    print()
    math = re.findall(r'\d\d\d[^.-]\d\d\d[^.-]\d\d\d\d',phone)
    print(math)

    print()
    lessRepitition = re.findall(r'\d{3}[.-]\d{3}[.-]\d{4}',phone)
    print(lessRepitition)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()