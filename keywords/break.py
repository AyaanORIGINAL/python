word = input("Enter a word: ")

for i in word:
    if i.lower() == 'a':
        print("A is found")
        break
    else:
        print('A isnt found')
    