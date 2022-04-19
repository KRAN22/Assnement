# generate armstrong numbers between 1 and 500

def armstrong(num):
    return sum([int(i)**len(str(num)) for i in str(num)]) == num

def noOfNUmber(num):
    for i in range(num):
        if armstrong(i):
            print(f"{i} is armstrong number")

noOfNUmber(5000)
