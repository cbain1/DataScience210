import sys
import random

# this prints the best song from Monty Python and the Holy Grail
def lumberjack():
    print ('I\'m a lumberjack and I\'m okay. ')
    print ('Sleep all night and work all day. ')
    print ('I\'m still a lumberjack, but now I just realized, I\'m not okay.')

def printTwice(lightning):
    print(lightning)
    print(lightning)

def creeper(yours, dates):
    if (yours/2+7 > dates):
        return True
    return False

def betterCreeper(yours, dates):
    # since this is a statement, it will either be true or false automatically
    return yours/2+7 > dates
    

# Define main for functions
def main():
    # print ('Hi')
    # lumberjack()
    # printTwice("Beep")
    # # prints 4 times per line
    # printTwice("DeprecationWarning"*4)
    a,b = input().split()
    print(creeper(int(a),int(b)))
    

if __name__ == '__main__':
    main()