import sys
import random



def main():
    fruit = 'bananas'
    letter = fruit[1]
    print(letter)

    # this has you reference the end of the string
    print(fruit[len(fruit)-1])
    # so does this
    print(fruit[-2]+fruit[-1])

    print((fruit*2)[-1])

    for i in fruit:
        print(i)

    for i in reversed(fruit):
        print(i)

    

if __name__ == '__main__':
    main()