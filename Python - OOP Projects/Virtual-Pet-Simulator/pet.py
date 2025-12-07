from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self,name,hunger,happiness):
        self.name=name
        self.hunger=hunger
        self.happiness=happiness

    def __str__(self):
        return f"Name:{self.name} |Hunger Level:{self.hunger} | Happiness Level:{self.happiness}"

    def feed(self):
        self.hunger-=10

        if self.hunger<0:
            self.hunger=0
        print(f"Hunger Level:{self.hunger}")

    def play(self):
        self.happiness+=10

        if self.happiness>100:
            self.happiness=100
        print(f"Happiness Level:{self.happiness}")

    def live_one_day(self):
        self.hunger+=5

        if self.hunger >=100:
            self.hunger = 100

        self.happiness-=5

        if self.happiness<=0:
            self.happiness=0

    def check_status(self):

        is_alive=True

        if self.hunger==100:
            is_alive=False

        if self.happiness==0:
            is_alive=False

        return is_alive

    @abstractmethod
    def speak(self):
        pass

class Cat(Pet):
    def __init__(self,name):
        super().__init__(name,50,50)

    def speak(self):
        return f"{self.name} says: Meow!"

    def __str__(self):
        base_str=super().__str__()
        return f"[CAT] {base_str}"

    def play(self):
        self.happiness += 5
        if self.happiness > 100:
            self.happiness = 100
        print(f"You tried to play with {self.name}, but they ignored you. (+5 Happiness)")

class Dog(Pet):
    def __init__(self,name):
        super().__init__(name,50,50)

    def speak(self):
        return f"{self.name} says: Havvvv!"

    def __str__(self):
        base_str=super().__str__()
        return f"[DOG] {base_str}"

    def play(self):
        super().play()
        print(f"{self.name} is wagging its tail enthusiastically! (+Extra happy)")
        self.happiness += 5
        if self.happiness > 100: self.happiness = 100
class Parrot(Pet):
    def __init__(self,name):
        super().__init__(name,50,50)
    def speak(self):
        return f"{self.name} says: 'Polly wants a cracker!'"
    def __str__(self):
        base_str=super().__str__()
        return f"[PARROT] {base_str}"