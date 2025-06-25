print("--- Enter the marks of the student ---")
subject1 = int(input("Enter the marks of subject 1:"))
subject2 = int(input("Enter the marks of subject 2:"))
subject3 = int(input("Enter the marks of subject 3:"))
subject4 = int(input("Enter the marks of subject 4:"))
subject5 = int(input("Enter the marks of subject 5:"))

total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5
print("The average marks is:", average)

if average >= 90 and average <= 100:
   print("Grade: A+")
elif average >= 80 and average <= 89:
    print("Grade: A")
elif average >= 70 and average <= 79:
    print("Grade: B")
elif average >= 60 and average <= 69:
    print("Grade: C")
elif average >= 50 and average <= 59:
    print("Grade: D")
elif average >=40 and average <= 49:
    print("Grade: E")
else:
    print("Grade: F")