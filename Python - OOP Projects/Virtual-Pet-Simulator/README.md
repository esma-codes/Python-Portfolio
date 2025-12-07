# Virtual Pet Simulator

A Python console-based Virtual Pet Simulator demonstrating core Object-Oriented Programming (OOP) concepts. Players adopt a pet (Cat, Dog, or Parrot) and manage its hunger and happiness levels day by day.

---

## 🚀 Features

- **Adopt a Pet:** Choose between Cat, Dog, or Parrot and give it a custom name.
- **Feed and Play:** Interact with your pet to reduce hunger and increase happiness.
- **Pet Speak:** Hear your pet “speak” with unique messages.
- **Day/Night Cycle:** Each day, pets get hungrier and their happiness decreases naturally.
- **Life Simulation:** Track your pet’s well-being; the game ends if hunger reaches 100 or happiness drops to 0.

---

## 💻 OOP Concepts Demonstrated

- **Abstraction:** `Pet` is an abstract base class (ABC) with abstract method `speak()`.
- **Inheritance:** `Cat`, `Dog`, and `Parrot` inherit from `Pet` and extend functionality.
- **Polymorphism:** Methods like `play()`, `feed()`, and `speak()` behave differently for each pet type.
- **State Management:** Tracks hunger and happiness levels, influencing the pet’s survival.

---