import sys
import random 
import re
#import regex -- strict supersset of re

# Define a main() function that prints a little greeting.
def main():

    #Regular expressions are a formalized "language" of templates you can use to search for a pattern in a larger documeent 
    #Soemtimes also called pattern matching
    #Gupta gave you a cheat sheet with some stuff to look at 

    print("\t this means a tab.")
    print(r"\t this is not a tab.") #This makes it a raw string and gets rid of the escape char patterns

    multilinestring = '''
        This is a multiline string.
        I like tacos.
        But tacos are expensive.
        I go to Taco Bell.
        But their tacos suck.
        I am amazing.
        Definitely not a narcissist.
        I have a mirror that does not reflect my personality.
        You and I on the other hand, have hands.
        '''
    print(multilinestring) #this prints with thr exact formatting you typed it with 

    #Thid is a reg ex for finding all new sentences 
    #The ^ means 'start of the line'
    for line in multilinestring.split("\n"):
        line = line.strip()
        if re.search('I',line):
            print("You are a narcissist.")

    # am now searching for taco
    count = 0
    for line in multilinestring.split("\n"):
        line = line.strip()
        if re.search('taco',line):
            count+=1
    print(count)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()