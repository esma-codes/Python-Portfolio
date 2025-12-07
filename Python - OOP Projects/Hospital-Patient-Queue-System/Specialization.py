from patient import Patient

class Specialization:

    status_dict={0:"Normal",1:"Urgent",2:"Super Urgent"}

    def __init__(self,name):
        self.name = name
        self.patients = []
        self.max_capacity=10

    def add_patient(self,patient,name,status):
        if len(self.patients)>=self.max_capacity:
            print(f"Cannot add {patient.name},Queue for {self.name} is full.")
            return
        if status not in self.status_dict:
            print("Invalid status. Status should be 0 (normal), 1 (urgent), or 2 (super-urgent).")
            return
        new_patient=Patient(name,status)
        self.patients.append(new_patient)
        self.patients.sort(key=lambda x:x.status,reverse=True)

        print(f"{patient.name} added to {self.name} specialization.")

    def remove_patient(self,name):
        for patient in self.patients:
            if patient.name==name:
                self.patients.remove(patient)
                print(f" {name} removed from {self.name} specialization.")
                return
        print(f"No patient found with the name {name} in {self.name}.")


    def get_next_patient(self):
        if len(self.patients)==0:
            print(f"No patient in {self.name} queue.")
            return None

        next_patient =self.patients.pop(0)
        print(f"Next patient: {next_patient.name} (status: {next_patient.status})")
        return next_patient

    def list_patients(self):
        if not self.patients:
            print(f"No patients in {self.name} queue.")
            return None
        for i,patient in enumerate(self.patients,start=1):
            print(f"{i}.{patient.name}-{self.status_dict[patient.status]}")

    def is_full(self):
        if len(self.patients) >= self.max_capacity:
            print(f"{self.name} specialization is full!")
            return True

        available = self.max_capacity - len(self.patients)
        print(f"{available} spots available in {self.name} specialization.")
        return False

















