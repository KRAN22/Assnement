
# 5. (greedy ? )
# 	farmer -> 3 daughters -> each daughter had a son
#         farmer had  mangoes in a room
#         farmer promisses his daughters that he is going distribute mangoes to them equally in the evening after his shopping.
#         In the absence of the father 1st daughter enters the room without the knowledge of her siblings
# 	She makes three divisions of the available mangoes in the room and 1 mango was extra she gives that to her child, takes 1 division(heap) and mixes other two divsions and leaves the room.
# 	Now 2nd daughter same idea and same execution
# 	Now 2rd daughter same idea and same execution
#        Finally the father enters the room and finds some mangoes and distributes it as he promised.

#   how many mangoes were there in the room? num1,num2,num3

# Generate 5 such numbers


cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 == 0:
            res = (num - 1) // 3 + 1
            lst.append(res)
            num = num - res
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} -->  remaining {} --> father distributes {} to each daughter".format(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 -->{}\n\t\tDaughter #3 --> {}".format(lst[0], lst[1], lst[2]))
        cntr += 1
    j += 1
