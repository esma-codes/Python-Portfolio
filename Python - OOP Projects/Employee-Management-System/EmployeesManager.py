from employee import Employee
class EmployeesManager:
    def __init__(self):
        self.employees=[]

    def add_employee(self):
        name = input("Enter employee name: ")
        surname=input("Enter employee surname: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))

        new_employee=Employee(name,surname,age,salary)
        self.employees.append(new_employee)

        print(f"{name} {surname} has been added successfully!")

    def list_employees(self):
        for emp in self.employees:
            print(emp)


    def delete_employee(self):

        name = input("Enter employee's name: ")
        surname = input("Enter employee's surname: ")

        for emp in self.employees:
            if emp.name==name and emp.surname==surname:
                self.employees.remove(emp)
                print("The operation was completed successfully.")
                return
        print(f"No employee found with the full name '{name} {surname}'.")


    def update(self):
        name = input("Enter employee's first name: ")
        surname = input("Enter employee's surname: ")

        for emp in self.employees:
            if emp.name==name and emp.surname==surname:
                new_salary=float(input(f"Enter new salary for {name} {surname}"))
                emp.salary=new_salary
                print(f"{name} {surname}'s salary updated to {new_salary}.")
                return

        print(f"No employee found with the name {name} {surname}.")

    def find(self):
        name = input("Enter employee's first name: ")
        surname = input("Enter employee's surname: ")

        for emp in self.employees:
            if emp.name==name and emp.surname==surname:
                print(emp)
                return

        print(f"No employee found with the name {name} {surname}.")

