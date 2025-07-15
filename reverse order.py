number = input("Enter a number: ")


if number.startswith('-'):
    number = number[1:]  

if number.isdigit():
  
    count = 0
    for digit in number:
        count = count + 1

    
    print("Your number has", count, "digits!")
else:
    print("Please type a whole number.")
