# Library Management System 

This project is a complete Library Management System built in Python, demonstrating core Object-Oriented Programming (OOP) principles. It allows a librarian to manage library items (books, magazines, DVDs) and members, and handle the process of lending and returning items.

This system is built as a console application and showcases advanced OOP concepts including Inheritance and Polymorphism.

## 🚀 Core Features

* **Item Management**: Add new books, magazines, or DVDs to the library inventory.
* **Member Management**: Register new members and remove existing ones.
* **Lending System**: Lend items to members. The system correctly tracks an item's availability.
* **Returning System**: Process item returns, making them available for other members.
* **Dynamic Listing**: List all items in the library or all registered members at any time.

## 💻 OOP Concepts Demonstrated

This project was specifically designed to practice and implement the fundamental pillars of OOP:

1.  **Encapsulation**: Each class (`Library`, `LibraryItem`, `Member`) bundles its own data (attributes) and behaviors (methods). For example, the `Library` class is solely responsible for the "business logic" of lending, while the `LibraryItem` class is only responsible for holding item data.
2.  **Inheritance**:
    * A parent class `LibraryItem` defines common attributes (`title`, `isbn`, `is_available`).
    * Child classes `Book`, `Magazine`, and `DVD` inherit from `LibraryItem` and extend it with their own specific attributes (`author`, `issue_number`, `director`).
3.  **Polymorphism**:
    * The `Library` class holds a single `self.all_items` list that can contain `Book`, `Magazine`, AND `DVD` objects.
    * A single method, `lend_item()`, can lend *any* type of `LibraryItem` without needing to know if it's a book or a DVD, thanks to polymorphism.
    * The `__str__` method is overridden in each child class to provide a custom, formatted output (e.g., `[BOOK]`, `[MAG]`).

