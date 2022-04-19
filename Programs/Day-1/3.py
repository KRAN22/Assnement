# 3. 1! = 1
#    2! = 2
#  145! = 1! + 4! + 5!
#       = 1  + 24 + 120
#       = 145
#   ?

# what is the next number which satisfies this condition

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum*=i
    return sum

def number(n):
    temp = str(n)
    sum = 0
    for i in temp:
      sum += factorial(int(i))
    return sum
      
print(number(145))
