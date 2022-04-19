# 1. write a code to generate identity matrix

def matrix(n):
    for row in range(0,n):
        for col in range(0,n):
            if row == col:
                print("1" ,end=" ")
            else:
                print("0", end=" ")
        print()
    
matrix(5)
    
