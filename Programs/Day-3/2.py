# 2.Write a Python script to check whether a given key already exists in a dictionary


def whether(dic):
    temp = []
    for i in dic:
        if i not in temp:
            temp.append(i)
    # print(temp)
    for i in temp:
        print(f"{i}'s in list : {dic.count(i)}")

dic = [1,2,3,1,3,1,4,1,3,1,3,3,1,2,3,1,2,1]
whether(dic)
