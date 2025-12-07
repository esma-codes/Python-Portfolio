class Employee:
    def __init__(self,name,surname,age,salary):
        self.name=name
        self.surname=surname
        self.age=age
        self.salary=salary

    def __str__(self):
        return f"Name:{self.name},Surname:{self.surname},Age={self.age},Salary:{self.salary}"