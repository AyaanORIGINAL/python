medical_cause = input("DO u have any medical cause? y or n: \n")

if medical_cause.lower() == "y":
    print("You are eligible for the exam.")
else:
    attendance_percentage = int(input("Enter your attendance percentage: "))
    if attendance_percentage >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")