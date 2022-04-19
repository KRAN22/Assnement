# 8. Remove all occurrences of a specific item from a list.

def occurrences(list,n):
    temp =[]
    for i in list:
        if i != n:
            temp.append(i)
    return temp

print(occurrences([1,2,3,4,5,1,4,5],1))
