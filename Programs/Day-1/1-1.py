# 01. print the pattern
# a.

# 1
# 23
# 456
# 78910

def pattern(n):
    val = 1
    for i in range(n):
        for j in range(i):
            print(val , end="")
            val += 1
        print()
pattern(5)
