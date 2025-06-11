name = "Lamine"
age = 17
weight = 70.49
isEmployee = True

print("Name:", name, "Data type of name is:",type(name))
print("Age:", age, "Data type of age is:",type(age))
print("Weight:", weight, "Data type of weight is:",type(weight))
print("isEmployee:", isEmployee, "Data type of isEmployee is:",type(isEmployee))

age = float(age)
weight = int(weight)
isEmployee = int(isEmployee)

print("\nAfter typecasting")
print("Name:", name, "Data type of name is:",type(name))
print("Age:", age, "Data type of age is:",type(age))
print("Weight:", weight, "Data type of weight is:",type(weight))
print("isEmployee:", isEmployee, "Data type of isEmployee is:",type(isEmployee))