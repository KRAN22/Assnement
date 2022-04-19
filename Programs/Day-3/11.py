# 11. Write a Python program to find the second smallest number in a list

def secondSmallNumber(list):
    n = len(list)
    small1 = small2 = list[0]
    for i in range(1,n):
        if list[i]<small1:
            small2 = small1
            small1 = list[i]
        elif list[i]< small2:
            small2 = list[i]
    return small2

print(secondSmallNumber([-1,2,1,-2,3,-1,-3,2,-4]))  
