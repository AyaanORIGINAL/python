valid = False

while not valid:
    try:
        user_input = input("Enter a number or enter q to leave: ")
        if user_input.lower() == "q":
            print("Goodbye")
            break
        n = int(user_input)
        if n >100 :
            print("bye")
            raise TypeError

    except TypeError:
        print("Invalid")