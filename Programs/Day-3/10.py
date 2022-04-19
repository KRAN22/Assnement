# Write a Python program to get the second largest number from a list

def secondLargeNumber(list):
    n = len(list)
    max1 = max2 = list[0]
    for i in range(1,n):
        if list[i]>max1:
            max2 = max1
            max1 = list[i]
        elif list[i] > max2:
            max2 = list[i]
    print(max1,max2)

secondLargeNumber([10,20,30,10,40,50,45])
