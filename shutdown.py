import os
choice = input("Do u want to shut down your device? (yes/no): ").lower()

if choice == "yes":
    print("Shutting Down")
    os.system("shutdown /s /t 3") 
elif choice == "no":
    print("Shutdown aborted.")
else:
    print("Invalid input. Please type 'yes' or 'no'.")

