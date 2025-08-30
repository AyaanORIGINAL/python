num = int(input("Enter a number: "))
user_input = input("Enter a list of odd numbers: ")

user_numbers = [int(x) for x in user_input.replace(",", " ").split()]

odd_numbers = [i for i in user_numbers if i % 2 != 0]

odd_under_num = [i for i in odd_numbers if i < num]

print("Odd numbers under", num, ":", odd_under_num)


fruits = ["apple", "banana", "mango", "orange", "grapes"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized list:", updated_fruits)

