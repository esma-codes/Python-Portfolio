from EmployeesManager import EmployeesManager

class FrontendManager:
    def __init__(self):
        self.manager=EmployeesManager()

    def menu(self):
        while True:
            print("\n--- Employee System Menu ---")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employee")
            print("4. Update Salary")
            print("5. Find Employee")
            print("6. Exit")

            choice=input("\nEnter your choice(1-6): ").strip()

            if choice=="1":
                self.manager.add_employee()
            elif choice == "2":
                self.manager.list_employees()
            elif choice == "3":
                self.manager.delete_employee()
            elif choice == "4":
                self.manager.update()
            elif choice == "5":
                self.manager.find()
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")



