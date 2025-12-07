from Specialization import Specialization
from patient import Patient


class OperationsManager:

    def __init__(self):
        self.specializations={"cardiology":Specialization("Cardiology"),
                             "neurology":Specialization("Neurology"),
                             "pediatrics": Specialization("Pediatrics")}

    def choose_specialization(self):
        print("Available Specialization: ")
        for i,name in enumerate(self.specializations.keys(),start=1):
            print(f"{i}-{name}")

        select_name=str(input("Enter specialization name: ")).lower()
        if select_name in self.specializations:
             return self.specializations[select_name]
        else:
            print("Invalid specialization!")
            return  None

    def print_menu(self):
        print("Program options: ")
        options=[
            "1-Add new patients",
            "2-Remove patient(s)",
            "3-Get next patient",
            "4-List all patients",
            "5-İs list full?",
            "6-Exit"
        ]
        print("\n".join(options))
        print(f"Enter your choice 1 to {len(options)} \n")

    def run(self):
        while True:
            self.print_menu()
            choice=int(input("Your choice: "))
            if choice==1:   #add patient
                spec = self.choose_specialization()
                if spec is not None:
                    name = input("Enter patient name: ")
                    status = int(input("Enter patient status (0=Normal,1=Urgent,2=Super-Urgent): "))
                    patient = Patient(name, status)
                    spec.add_patient(patient,name,status)


            elif choice == 2:  # Remove patient
                spec = self.choose_specialization()
                if spec:
                    name = input("Enter patient name to remove: ")
                    spec.remove_patient(name)

            elif choice == 3:  # Get next patient
                spec = self.choose_specialization()
                if spec:
                    spec.get_next_patient()

            elif choice == 4:  # List all patients
                spec = self.choose_specialization()
                if spec:
                    spec.list_patients()

            elif choice == 5:  # Is list full?
                spec = self.choose_specialization()
                if spec:
                    spec.is_full()

            elif choice == 6:  # Exit
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Try again.")



