import sys

def main ():
    x = input('What is your favorite number? ' )
    print (type(x),x)
    x = int(x)
    print (type(x), x)

    if x<5:
        print ('You dream too small, shawty.')
        print ('Go Away.')
    elif x==7:
        print ('You broke the sacred Thomas rule. You fail.')
    # To write a double boolean phrase, tis not the name as python 
    elif x<18 & x>20:
        print('You broke math...')
    # To check if something is not equal, use != same as C++
    elif x<25:
        print ('You dream in a medium size.')
        print ('Much like the coke you get in a combo meal at Taco Bell.')
    else:
        print('You dream an adequate amount.')


if __name__ == '__main__':
    main()