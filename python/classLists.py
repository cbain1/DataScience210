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
    #if you say x in c... this creates a list from 0 to length c

    # ah yes, two lines of code that do literally nothing
    for x in []:
        print('hi')

    print('-'*10)

    #--------------

    #look, more proof that lists are just strings
    print([1,2]+[3,'random'])
    print([1,2,',']*4)

    # Look, you can use slices
    print(c[:])
    print(c[1:3])

if __name__ == '__main__':
    main()