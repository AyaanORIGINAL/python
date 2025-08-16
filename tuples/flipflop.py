def flip_flop(tup):
    first = 0
    last = len(tup) - 1
    while(first < last):
        if tup[first] != tup[last]:
            return False
        first += 1
        last -= 1
    return True

t = (1,2,3,3,2,1)
result = flip_flop(t)
if result == True:
    print("The tuple is a flip-flop tuple.")
else:
    print("The tuple is not a flip-flop tuple.")