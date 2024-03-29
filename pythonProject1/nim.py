# Henry Voter and Tianze Ren (hwv4ug and tr2bx)
# Lab 100


# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

marbles = 0
pick = 0


def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while ans <= n:
        ans *= 2
    return int(ans / 2)


print("The Game of Nim\n")
marbles = int(input("The number of marbles in the pile: "))
turn_choice = input("Who will start? (p or c): ")
turn = False
if turn_choice == 'p':
    turn = True

while marbles != 0:
    print("The pile has", str(marbles), "marbles in it.")
    if turn:
        can_take = marbles // 2

        take = int(input("How many marbles do you want to take (1-" + str(can_take) + "): "))
        while take < can_take:
            marbles -= take
            can_take = 0

    else:
        take = 1
        target = pow2(marbles)
        take = marbles - target
        if take < 1:
            take = 1
        marbles -= take
    print("The computer takes", take, "marbles.")

    turn = not turn

if turn:
    print("The player wins!")
else:
    print("The computer wins!")