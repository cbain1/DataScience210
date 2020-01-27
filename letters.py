import sys
import random

# Define main for loops, bro
def main():
    
    phrase = input("Please enter letters and spaces and what not: ")
    letter = input("now tell me your letter: ")

    count = 0

    for i in phrase:
        if i == letter:
            count+=1

    print("There are ", count, " of that letter in your phrase.")



if __name__ == '__main__':
    main()