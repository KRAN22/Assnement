# b.

# 1
# 22
# 333
# 4444
# 55555

def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end="")
        print()

pattern(5)
pattern(6)
