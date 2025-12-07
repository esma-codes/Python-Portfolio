# 👩‍💼 Employee Management System

This project is a **Python Object-Oriented Programming (OOP)** example I created to practice and demonstrate the core OOP principles — **encapsulation**, **composition**, and **modularity**.  
It simulates a simple employee management system that allows users to manage employee information interactively.

---

## 🎯 Project Purpose

The goal of this project is **not only to manage employee data**, but also to **understand how to apply OOP concepts** in a real-world scenario.

In this project, I designed multiple classes, each with a clear responsibility, and connected them through composition.  
I focused on writing clean, modular, and easy-to-understand Python code — just like in real-world applications.

---

## ⚙️ Features and My Implementation Approach

### 🟢 1. Add New Employees  
I used `input()` functions to collect data (name, surname, age, salary) from the user.  
Each employee is represented by an **`Employee` object**, and I store them inside a list `self.employees` in the **`EmployeesManager`** class.  
This allows dynamic creation and management of employee data.

---

### 🔵 2. List All Employees  
The `list_employees()` method loops through `self.employees` and prints each object.  
I also defined a `__str__()` method in the `Employee` class to control how the employee information is displayed neatly.

---

### 🔴 3. Delete Employees by Name and Surname  
I wanted the deletion to be **accurate**, not just based on the first name.  
So I used **both `name` and `surname`** for identification.  
The program searches the list and removes the matching employee object.  
This mimics how real HR systems identify people uniquely.

---

### 🟣 4. Update Employee Salary  
In the `update()` method, I first find the employee by name and surname.  
If found, the program asks for a new salary and updates it directly on that object.  
This shows how objects can be **modified dynamically** after creation — a key OOP concept.

---

### 🟠 5. Find Employee Details  
The `find()` method searches through the employee list and displays the employee that matches the given name and surname.  
This demonstrates the concept of **object lookup** inside a collection.

---

## 💡 OOP Concepts I Practiced

- **Encapsulation:**  
  Each employee’s data (name, surname, age, salary) is stored safely inside the `Employee` class.

- **Composition:**  
  The `EmployeesManager` class contains a list of `Employee` objects.

- **Abstraction:**  
  The `FrontendManager` hides the complexity of the backend and provides a simple menu for users.

- **Modularity:**  
  The project is divided into multiple Python files, making the code cleaner and easier to maintain.

---
