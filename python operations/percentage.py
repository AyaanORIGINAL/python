math = int(input("Enter the marks of math: "))
history = int(input("Enter the marks of history: "))
science = int(input("Enter the marks of science: "))
english = int(input("Enter the marks of english: "))

percentage = ((math + science + history + english)/400)*100

print("The percentage of the student is: ", percentage, "%")