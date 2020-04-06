import sys
import random



def main():
   
    greetings = 'Welcome to Mondday! :)'
    #greetings[0] = 'H'
    #Explicitly defined strings in Python are immutable, which means that is cant be changed! Which is why the above line cannot be fixed

    #So, how do you find out what string options there are -- use dir which will list all the things you can do to the given object
    print(dir(greetings))

    # Help gives you help
    print(help(str.capitalize))


if __name__ == '__main__':
    main()