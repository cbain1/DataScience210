#!/usr/bin/python3 -tt
# Ankur Gupta

"""
Generates the huge lists for Project 1
"""

import sys
import random

def main():
    filename = sys.argv[1]
    if len(sys.argv) >= 3:
        size = int(sys.argv[2])
    else:
        size = 100000

    numbers = random.sample(range(1,10000000), size)
    numbers.sort()
    
    fout = open(filename, "w+")
    fout.write("%s\n" % size)
    for x in numbers:
        fout.write("%s\n" % x)
    fout.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()