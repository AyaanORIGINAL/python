weight = float(input("Enter your weight in kg: "))
height = float (input("Enter your height in meters: "))

BMI = weight / (height ** 2)
print("Your BMI is: ", BMI)

if BMI < 18.5:
   print("You are underweight")
elif BMI <= 24.5:
   print("You are normal weight")
elif BMI <= 29.9:
   print("You are overweight")
elif BMI <= 34.9:
   print("You are obese")
elif BMI <= 39.9:
   print("You are severely obese")
else:
   print("You are morbidly obese")