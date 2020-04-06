import sys


def main():
    # a dictionary (also called a has table) is like a list, so much so its almost the "same" as a list 
    # but also its super different 
    # the index for a dictionary can be ~anything~
    # its also like super powerful and is a data structure
    # a data scructure is an object containing data in a very specific way - how to organize data
    # example: an array is a data scructure 

    # the index of a dictionary is commonly called a key 
    # the element at that key is commonly called a value

    l33t2eng = {} # this is a dictionary 
    l33t2eng['fox'] = "'good lookin' person"

    # you can also fill a dictionary this way 
    l33t2eng = {'scrooging':'breaking up to save yourself money','n00b':'person who sucks at games','suxxors':'you suck','git gud':'get good','rigged':'i didn\'t win the impossible game and i\'m mad about it '}
    print(l33t2eng)

    # you can do lots of things with dictionaries 
    # you can find out what you can do with the help menu 
    print(len(l33t2eng)) #this will give you 5

    # you can also use the 'in' expression to find keys in the dict  
    # you cannot search for values though 

    # the less good way of printing all values
    for key in l33t2eng:
        print(l33t2eng[key])
    
    # the more pythonic way of printing all values 
    for value in l33t2eng.values():
        print(value)

    # if you want to do both things, you can do this 
    for key,value in l33t2eng.items():
        print(key, ":", value)
        
    
    # let's do an exercise  - tell me how many of each letter are in the following words
    words = 'supercalifragiliciousexpealidocious paraskivatriaphobia'
    letterCount = {}
    for letter in words:
        if letter in letterCount: 
            letterCount[letter]+=1
        else:
            letterCount[letter]=1
    print(letterCount)

    keyList = list(letterCount.keys())
    print(keyList)
        
    keyList.sort()

    for letter in keyList:
        print(letter,letterCount[letter])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()