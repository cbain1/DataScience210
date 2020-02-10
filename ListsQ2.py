import sys
import random

def beret(request):
        total = 0
        strings = 0
        #Loops through all words in request
        for elem in request: 
            count =0
            #splits each word into its own string value
            word = list(elem)
            # this loops through each letter in each word to see the number of letters in each word
            for elem in word:
                count +=1
            total += count
            strings +=1
        average = total/strings

        return (average)

# Define main for loops, bro
def main():

    request = ['lists', 'are', 'pretty', 'cool', 'well', 'as', 'cool', 'as', 'computer', 'science', 'gets', 'which', 'is', 'not', 'very', 'cool' ]
            

    print("Your average number of letters is: ", beret(request))

if __name__ == '__main__':
    main()

"""
catherinebain > python3 ListsQ2.py
Your average number of letters is:  4.1875
"""