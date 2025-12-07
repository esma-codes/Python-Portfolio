# Restaurant Order & Billing System

This is a complete, console-based application for managing a restaurant's orders and billing, built entirely in Python using Object-Oriented Programming (OOP).

The system simulates a restaurant environment where a user (waiter) can manage orders for a specific table. It handles different types of menu items (e.g., food, drinks) and can accurately calculate the total bill for a table at any time.

## 🚀 Core Features

* **Dynamic Menu:** The system is built on a "parent" `MenuItem` class, allowing for different item types like `Food` and `Drink` to be added.
* **Order Management:** Add or remove items from a table's specific order.
* **Polymorphic Lists:** The order list (`Order` class) seamlessly manages both `Food` and `Drink` objects in the same list.
* **Automatic Bill Calculation:** Instantly calculate the total price of all items in a table's order by calling a single method.

## 💻 OOP Concepts Mastered in This Project

This project was designed to be a comprehensive test of fundamental and advanced OOP principles:

1.  **Encapsulation**:
    * Each class (`Table`, `Order`, `MenuItem`) bundles its own data and the methods that operate on that data.
    * For example, the `Order` class is solely responsible for its `self.items` list and the logic for `calculate_total()`. The `Table` class doesn't know *how* the total is calculated; it simply asks the `Order` object for the result.

2.  **Inheritance (IS-A Relationship)**:
    * A parent class, `MenuItem`, defines common attributes (`item_id`, `name`, `price`).
    * Child classes, `Food` and `Drink`, inherit from `MenuItem` using `super()` and extend it with their own specific attributes (`category` for Food, `size_ml` for Drink).

3.  **Polymorphism (Many Forms)**:
    * The `Order` class's `self.items` list holds a mix of `Food` and `Drink` objects.
    * The `calculate_total()` method iterates over this mixed list and calls `.price` on each object. It works perfectly without ever needing to check `if type(item) == Food`.

4.  **Composition (HAS-A Relationship)**:
    * This is the core of the project's design. Instead of `Table` *being* an `Order`, a `Table` *has-a* (owns) an `Order` object.
    * In `table.py`, the `Table` class's `__init__` method creates its own instance of the `Order` class: `self.order = Order()`.
    * When a `Table` needs to add an item, it *delegates* the task to its `Order` object (e.g., `self.order.add_item(...)`).