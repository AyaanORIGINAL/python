class Employee:
    def __init__ (self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
        print(f"Employee {self.name}(ID: {self.emp_id} created)")

    def __del__(self):
        print(f"Employee {self.name}(ID: {self.emp_id} deleted)")

def create_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    emp = Employee(name, emp_id)
    return emp
print("Creating employee")
emp1 = create_employee()
emp2 = create_employee()
print("End of program. Deleting employees") 
