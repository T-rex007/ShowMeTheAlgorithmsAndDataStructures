def factorial(n):
    if(n == 1):
        return 1
    else:
        return n*factorial(n-1)

def revString(s):
    if(len(s) == 0):
        return s
    else:
        return revString(s[1:]) + s[0]

def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair -4) +
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )