
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

def pattern(n):
    for i in range(1, n+1):
        for space in range(n-i):
            print(" ", end="")
        for j in range(1,i+1):
            print(j ,end=" ")
        print()
    for i in range(n,1,-1):
        for space in range(n-i+1):
            print(" ",end="")
        for j in range(1,i):
            print(j ,end=" ")
        print()

pattern(5)
