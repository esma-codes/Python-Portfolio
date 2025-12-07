from products import Electronics, Clothing,Book
from customer import Customer

def create_store_inventory():

    inventory=[
        Electronics("E-1001", "Asus ROG Strix Laptop", 25000.0, "24 months"),
        Electronics("E-1002", "Samsung QLED TV", 18000.0, "36 months"),
        Clothing("C-2001", "Blue T-Shirt", 350.0, "L", "Blue"),
        Clothing("C-2002", "Black Jeans", 800.0, "M", "Black"),
        Book("B-3001", "Dune", 150.0, "Frank Herbert"),
        Book("B-3002", "1984", 100.0, "George Orwell")
    ]

    return inventory

def print_menu():
    print("\n--- E-Commerce Store Menu ---")
    print("1. View All Products (Store Inventory)")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Your Shopping Cart")
    print("0. Exit Store")

def list_products(inventory):
    print("\n--- Available Products in Store ---")
    for item in inventory:
        print(item)


def find_product_by_id(product_list, product_id):
    """
    Helper function to find a product in ANY list by its ID.
    """
    for item in product_list:
        if item.product_id == product_id:
            return item
    return None


def handle_add_to_cart(customer, inventory):
    list_products(inventory)
    product_id = input("Enter the Product ID to add to cart: ").strip().upper()

    product_to_add = find_product_by_id(inventory, product_id)

    if product_to_add:
        customer.add_to_cart(product_to_add)
    else:
        print(f"ERROR: Product with ID '{product_id}' not found in store.")


def handle_remove_from_cart(customer):
    if not customer.cart.items:
        print("Your cart is already empty.")
        return

    customer.view_cart()
    product_id = input("Enter the Product ID to remove from cart: ").strip().upper()

    product_to_remove = find_product_by_id(customer.cart.items, product_id)

    if product_to_remove:
        customer.remove_from_cart(product_to_remove)
    else:
        print(f"ERROR: Product with ID '{product_id}' not found in your cart.")


def main():
    store_inventory = create_store_inventory()

    customer_name = input("Welcome to the store! Please enter your name: ").capitalize()
    current_customer = Customer(customer_name, "C-001")

    while True:
        print_menu()
        choice = input(f"Hello {current_customer.name}, what would you like to do? (0-4): ")

        if choice == '1':
            list_products(store_inventory)

        elif choice == '2':
            handle_add_to_cart(current_customer, store_inventory)

        elif choice == '3':
            handle_remove_from_cart(current_customer)

        elif choice == '4.':
            current_customer.view_cart()

        elif choice == '0':
            print(f"Thank you for shopping with us, {current_customer.name}. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")


if __name__ == "__main__":
    main()

