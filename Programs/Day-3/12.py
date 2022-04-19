# 12. Write a Python program to get unique values from a list.

def uniqueNumber(list1):
    num = set(list1)
    return list(num)
print(uniqueNumber([1,2,3,4,1,2,3]))
