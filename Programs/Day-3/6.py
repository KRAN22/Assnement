# 6. Write a code to get the key of a minimum value from a dictionary

def minimum(dic):
    temp = []
    for key ,val in dic.items():
         temp.append(val)
    min= temp[0]
    for i in range(len(temp)):
        if temp[i]< min:
            min = temp[i]
    return min

print(minimum({"1":1,"2":10,"3":-1,"3":-2}))
