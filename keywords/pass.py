for i in range(1,21):
    if i % 20 == 0:
        print("Twist")
    elif i % 15 == 0:
        pass
    elif i % 10 ==0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        pass
    else:
        print (i)