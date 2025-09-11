class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, ID Number: {self.id_number}")

class Employee(Person):
    def __init__(self, name, id_number, salary, position):
        super().__init__(name, id_number)
        self.salary = salary
        self.position = position
    def display_emp_info(self):
        self.display_info
        print(f"Salary: {self.salary}, Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, id_number, salary, position, team_size):
        super().__init__(name, id_number, salary, position)
        self.team_size = team_size

    def display_emp_info(self):
        super().display_emp_info()
        print(f"Team Size: {self.team_size}")
emp1 = Employee("MIntu", "7171", 2, "Intern")
manager1 = Manager("Raju", "7170", 50000000, "Team Leader", 10)
emp1.display_emp_info()
print()
manager1.display_emp_info()
