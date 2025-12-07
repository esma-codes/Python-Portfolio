class Patient:
    def __init__(self,name,status):
        self.name=name
        self.status=status

    def __str__(self):
        print(f"Name:{self.name}-Statu:{self.status}")

