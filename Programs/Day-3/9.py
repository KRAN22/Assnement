# Write a Python program to sum all the items in a list

def sumNumber(list):
    sum = 0
    for i in list:
        sum += i
    return sum
    
print(sumNumber([1,2,3,4]))
