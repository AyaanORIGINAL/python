import random

length = int(input("Enter password length: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""
for i in range(length):
    password += random.choice(characters)

if length < 8:
    print("Password should include at least 8 characters.")
else:
    print("Generated password:", password)