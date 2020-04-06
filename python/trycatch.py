import sys
import random


# Define main for try/except bro
def main():
    temp = input('Enter the current temperature: ')
    try:
        far = float (temp)
        cel = (far - 32.0)*(5.0/9.0)
        print(cel)
    except:
        print ('Please enter a number, not ', temp, '.')


if __name__ == '__main__':
    main()