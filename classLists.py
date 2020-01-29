import sys
import random

# Define main for loops, bro
def main():
    
    c = [10,20,30,40]
    print(c)

    d = ['frog','cat','taco','burrito']
    print(d)

    listception = [c,d,c]
    print(listception)

    listlistception = [listception]
    print(listlistception)

    #lits dont have to have the same stuff in it
    f = ['spam', 2.5, [c]]
    print(f)
    empty = [] #look an empty list

    c[1] = 'orange'
    print(c) #look i changed the entry in the first position of the list

    #Boolean on lists
    print(5 in f)
    print(20 in f)
    print('spam')

    #print all of list c do this.... or just print c
    for x in c:
        print(x)

if __name__ == '__main__':
    main()