import sys


# Define main for loops, bro
def main():


    def merge():

        file1 = open("list1.txt")
        file2 = open("list2.txt")

        # get length from first line of file
        length1 = int(file1.readline())
        length2 = int(file2.readline())

        #copy files to lists
        list1 = []
        list2 = []
        for line in file1:
            list1.append(int(line))
        for line in file2:
            list2.append(int(line))
    
        merged = [] 
        i, j = 0, 0
        same = 0
    
        while i < length1 and j < length2: 
            if list1[i] < list2[j]: 
                merged.append(list2[i]) 
                i += 1
        
            elif list2[j] < list1[i]: 
                merged.append(list2[j]) 
                j += 1
            else:
                merged.append(list1[i])
                i+=1
                j+=1
    
        merged = merged + list1[i:] + list2[j:] 
        
        return merged

    if (len(merge()) <25):
        print(merge())
    else:
        print(len(merge()))
    print


if __name__ == '__main__':
    main()




# catherinebain > python3 ListsQ3.py
# 236631


