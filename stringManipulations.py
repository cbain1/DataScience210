import sys

def main ():
    s = 'spam,'
    s = s*4
    print(s)
    delimiter = ','
    t = s.split(delimiter)
    print(t)



    #Find out who likes Gupta enough to email him 
    fhand = open('mbox-short.txt')
    emailList = []
    for line in fhand:
        line = line.rstrip() #strips trailing whitespace and then stores the line
        #continue skips the current letter and then moves on to the next
        if not line.startswith('From:'): continue
        #so if we made it here in the loop, the line starts with from 
        email = line.split()
        emailList.append(email[1])
    print(emailList)
    

if __name__ == '__main__':
    main()