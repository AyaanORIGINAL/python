import random

length = int(input("Enter password length: "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""
for i in range(length):
    password += random.choice(letters)

print("Generated Password:", password)


