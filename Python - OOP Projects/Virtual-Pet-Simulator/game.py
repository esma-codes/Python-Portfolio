from pet import Cat,Dog,Parrot

class Game:
    def __init__(self):
        choice=input("Choose your pet: 1. Cat 🐱, 2. Dog 🐶,  3. Parrot 🦜: ")

        pet_name = input("What will you name your pet? ")

        if choice=="1":
            self.pet=Cat(pet_name)
            print(f"You adopted a dog named {self.pet.name}!")

        elif choice == '2':
            self.pet = Cat(pet_name)
            print(f"You adopted a cat named {self.pet.name}!")

        elif choice == '3':
            self.pet = Parrot(pet_name)
            print(f"You adopted a parrot named {self.pet.name}!")

        else:
            print("Invalid choice! You get a generic pet rock.")
            self.pet = Dog("Rocky")

    def start_game(self):
        day_count = 1
        while True:
            print("\n--- Day Start ---")
            print(self.pet)
            print("\n")
            print("Actions: [1] Feed 🍖\n, [2] Play 🎾\n, [3] Speak 🗣️\n, [0] Quit ❌")
            choice=input("Choose an process: ")

            if choice=="1":
                self.pet.feed()
            elif choice=="2":
                self.pet.play()
            elif choice=="3":
                print(self.pet.speak())
            elif choice=="0":
                print("Terminate the program")
                break
            else:
                print("Invalid input!")
                continue

            #----------Flow of time-------------------
            print("\n🌙 Night comes... Time passes...")
            self.pet.live_one_day() #The animal gets hungry and bored by itself.
            day_count += 1

            #-------------Control of life------------
            if not self.pet.check_status():
                #If check_status returned False, the animal has died.
                print(f"\nGAME OVER! {self.pet.name} has passed away...")
                print(f"Survived for {day_count - 1} days.")

                print(f"Final Status: {self.pet}")
                break



