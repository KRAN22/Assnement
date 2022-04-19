# 13. Write a Python program to get count of repetition of each value from a list.


def repetitionNumbers(list ,x):
    count = 0
    for i in list:
        if i == x:
            count +=1
    return count

print(repetitionNumbers([1,2,3,1,3,1,3,2,1,1,1,1],1))
