import sys


def main():

    #List methods
    t = ['a','b','c','d','e']
    t.append('f')
    print(t)

    t2 = ['g','h']
    t.extend(t2)
    print(t)

    t.sort() #this sorts the list into nondecreasing order

    # pop removes an item from list t at a given index and returns it 
    popped = t.pop(1)
    print(popped)
    print(t)
    #By defauly, pop removes the last element of the list 

    #Another way to 'pop' is to use del -- which is from python2 -- but del also allows you to 'pop' slices of lists
    del t[1:3]
    print(t)

    t.remove('e') #this removes e
    # t.remove('w') # this will make it yell at you bc you cannot remove things that are not there
    #also this will only remove one occurence, you must manually commit item genocide if you wish

    numList = [-45,1,2,3,4,5,9001,54]
    print(numList)
    print(max(numList))
    print(min(numList))
    print(sum(numList))

if __name__ == '__main__':
    main()