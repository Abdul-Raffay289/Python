def palind(r):
    s = 0
    e = len(r) - 1
    while s < e:
        if (r [s] != r [e]):
            return False
        s+=1
        e-=1
    return True
r = (1, 2, 3, 3, 2, 1)
if(palind(r)):
    print("Tuple is Flip Flop")
else:
    print("Tuple is not Flip Flop") 