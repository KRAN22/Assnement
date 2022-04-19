# 4. write a code to generate pascals triangle

#             1
#            1 1
#           1 2 1
#          1 3 3 1
#         1 4 6 4 1


def pattern(n):
    for i in range(n+1):
        for j in range(0,n-i+1):
            print(" ",end="")
        c = 1
        for j in range(1,i+1):
            print(c,end=" ")
            c = c *(i-j)//j 
        print()

pattern(5)
