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
    alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for letter in words:
        if letter in alphabet:
            alphabet[letter]+=1
    # you can then continue this pattern for the rest of the alphabet
    print(alphabet)

        





# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()