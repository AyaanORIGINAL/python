def factorial(num):
    '''This is a function that calculates factorial recursively'''

    if num == 0 or num == 1:
       return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(5))
print (factorial(4))
print(factorial.__doc__)