import sys

def main():

    first, second = input("Please enter two words " ).split()
    print("The new name for the school previosly known as Hogwarts is: " + first+second)

# Truncation simply chops off the end of a given value (i.e. truncation would turn both 2.7 and 2.2 into 2) whereas rounding uses the rules of math to change the value to the closest number (i.e. rounding would turn 2.7 into 3 while it would turn 2.2 into 2)

#type is a way of figuring out what class a certain variable is i.e. whether the variable is an integer or a double or a string value


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

