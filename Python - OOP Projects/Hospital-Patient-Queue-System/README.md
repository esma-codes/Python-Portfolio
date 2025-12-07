# Hospital Patient Queue Management System

## Overview
The **Hospital Patient Queue Management System** is a Python-based command-line application designed to manage patient queues in a hospital setting. This project demonstrates the use of **Object-Oriented Programming (OOP)** principles and provides a simple yet effective way to handle patient data and queue management.

The system includes three main classes:

1. **Patient**: Represents an individual patient with a name and a status.
2. **Specialization**: Manages patient queues within different hospital departments and handles operations like adding, removing, and retrieving patients.
3. **OperationsManager**: Serves as the user interface, allowing users to interact with different specializations and perform actions such as adding patients, listing patients, or getting the next patient.

---

## Features

- **Add new patients**  
  Patients can be added to a specific specialization (department). Each patient has a **status** indicating urgency:
  - `0` → Normal
  - `1` → Urgent
  - `2` → Super-Urgent  
  The system automatically positions patients in the queue based on their urgency.

- **Remove patients by name**  
  Users can remove patients from a specialization by providing the patient’s name.

- **Get the next patient**  
  Retrieves the next patient from a specialization queue according to priority.

- **List all patients**  
  Displays all patients currently in a specialization queue, along with their status.

- **Check if the queue is full**  
  Each specialization has a maximum capacity (default 10). Users can check if the queue is full or how many spots are available.

- **Exit**  
  Gracefully ends the program.

---