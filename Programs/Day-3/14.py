# 14. Write a Python program to find common items from two lists.

def commonItem(color1,color2):
    commonNumbers = set(color1)& set(color2) 
    return list(commonNumbers)

print(commonItem([1,2,3,4,5],[1,2,5,6,7,8,9]))
