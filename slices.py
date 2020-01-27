import sys
import random



def main():
    s = 'that is a heathen statement'
    # these are slices, which let you reference only a portion of a given string
    print(s[0:6])
    print(len(s))
    print(s[6:27])
    print(s[6:len(s)])

    # if you don't put the right side, it goes to the end, same with if you don't put the beginning, it defaults to the beginning
    print(s[6:])

    #look this prints the whole thing
    print(s[:])


    #more slicing please -- after the second colon, that number tells you how many they want you to iterate by
    print(s[::3])
    print(s[::-1]) #this prints backwards
    print(s[::-2])

    print(s[10:3:-3]) # the end number is non-inclusive

if __name__ == '__main__':
    main()