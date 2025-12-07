from ShoppingCart import ShoppingCart

class Customer:
    def __init__(self,name,id):
        self.name=name
        self.customer_id=id
        self.cart=ShoppingCart()

        print(f"Customer '{self.name}' created with an empty shopping cart.")

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"

    def add_cart(self,product):
        self.cart.add_item(product)
        print(f"{product.name} is added in the cart.")
    def remove_cart(self,product):
        self.cart.remove_item(product)
        print(f"{product.name} is removed in the cart")
    def view_cart(self):
        print(f"\n--- {self.name}'s Cart ---")
        self.cart.list_item()
        total=self.cart.calculate_total()
        print(f"----------------------------")
        print(f"TOTAL PRICE: {total:.2f} TL")

