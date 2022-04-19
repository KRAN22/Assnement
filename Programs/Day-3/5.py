# 5. Write a Python program to remove duplicates (values) from Dictionary

def removeDuplicates(dic):
    temp = []
    res = {}
    for key, val in dic.items():
        if val not in temp:
            temp.append(val)
            res[key] =  val
    return res

print(removeDuplicates({"a":10,"b":20,"c":30,"d":20}))
