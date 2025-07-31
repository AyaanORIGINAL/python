valid = False

while not valid:
    try:
        n = int(input("enter a number: "))
        if n >100 :
            print("bye")
            raise TypeError

    except TypeError:
        print("Invalid")