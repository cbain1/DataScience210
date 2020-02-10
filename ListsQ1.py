import sys

def main():

    request = input("Please enter a string of upper/lowercase letters and spaces: " )
    letters = list(request)

    # delete spaces
    def deletrius(letters):
        merged = []
        for x in letters: 
            if ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')):
                merged.append(x)
        return merged

    # make it grow
    def engorgio(letters):  
        merged = []
        merged = deletrius(letters) 
        for x in range(len(merged)): 
            if (merged[x] >= 'a' and merged[x] <= 'z'):
                char = ord(merged[x]) - 32
                merged[x] = chr(char) 
        return merged
    # case sensitive palindrome
    def priori(letters):
        merged = []
        reverseLow = []
        merged = deletrius(letters)
        for x in range(len(merged)-1,-1,-1):
            reverseLow.append(merged[x])
        return reverseLow == merged
  

    #case insensitive palindrome
    def prioriincantantum(letters):
        merged = []
        reverseHigh = []
        merged = engorgio(letters)
        for x in range(len(merged)-1,-1,-1):
            reverseHigh.append(merged[x])
        return reverseHigh == merged


    print ("The statement that your word is a palindrome is ", priori(letters))
    print ("The statement that your word is a case insensitive palindrome is ", prioriincantantum(letters))





if __name__ == '__main__':
    main()



"""
catherinebain > python3 ListsQ1.py
Please enter a string of upper/lowercase letters and spaces: mOm
The statement that your word is a palindrome is True
The statement that your word is a case insensitive palindrome is True
catherinebain > python3 ListsQ1.py
Please enter a string of upper/lowercase letters and spaces: m     OM
The statement that your word is a palindrome is False
The statement that your word is a case insensitive palindrome is True
catherinebain > python3 ListsQ1.py
Please enter a string of upper/lowercase letters and spaces: m         o        M
The statement that your word is a palindrome is False
The statement that your word is a case insensitive palindrome is True
catherinebain > 
"""