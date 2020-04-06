import sys

def condition (i,j,length1,length2):
    return (i < length1 and j < length2)

def merge(list1, list2):
    merged = [] 
    length1 = len(list1)
    length2 = len(list2)
    i=0
    j=0

    while condition(i,j,length1,length2): 
        if len(merged) > 0:
            while (list1[i]==merged[len(merged)-1] or list2[j]==merged[len(merged)-1]):
                if(list1[i]==merged[len(merged)-1]):
                    i+=1
                    if not condition(i,j,length1,length2):
                        break
                elif(list2[j]==merged[len(merged)-1]):
                    j+=1
                    if not condition(i,j,length1,length2):
                        break
        if not condition(i,j,length1,length2):
            break
        elif list1[i]==list2[j]:
            merged.append(list1[i])
            i+=1
        elif list1[i] < list2[j]: 
            merged.append(list1[i]) 
            i += 1
        elif list2[j] < list1[i]: 
            merged.append(list2[j]) 
            j += 1 

    while (i>=length1 and j<length2):
        if(list2[j]==merged[len(merged)-1]):
            j+=1
        else:
            merged.append(list2[j])

    while (j>=length2 and i<length1):
        if(list1[i]==merged[len(merged)-1]):
            i+=1
        else:
            merged.append(list1[i])
    
    return merged

# Define main for loops, bro
def main():

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

    if (len(merge(list1,list2)) <25):
        print(merge(list1,list2))
    else:
        print(len(merge(list1,list2)))


if __name__ == '__main__':
    main()

    


"""
catherinebain > python3 ListsQ3.py
236629
"""

