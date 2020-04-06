

import sys
import random

# Define main for loops, bro
def main():
    # random.random() returns a number uniformly from [0,1]
    x = random.random()
    print(x)
    print()

    n = 1
    while n < 10:
        print(random.random())
        n+=1
    
    # Range command creates integers within that range

    for i in range(10):
        print(random.randint(100,120))

    
    print ('Taco Bell Nightmare')
    print ('Burger King Fries are Better')

    t = ['taco', 'burrito', 'nachos', 'tequila']

    for i in t:
        print('fight me', i)


    for x in range(10):
        print(10-x)
        x+=1
    print ('Look, its the New Year, but also time is a social construction so really that means nothing')


    # Stuff about range
    # -1 here is the increment, aka each loop decreases by 1
    for x in range(15,2,-1):
        print(x)
        


if __name__ == '__main__':
    main()