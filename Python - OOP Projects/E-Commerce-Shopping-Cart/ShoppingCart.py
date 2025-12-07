from products import Product

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)
        print(f"'{item.name}' added to cart.")

    def remove_item(self,item):
        self.items.remove(item)
        print(f"'{item.name}' deleted to cart.")

    def list_item(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(item)

    def calculate_total(self):
        total_price=0
        for item in self.items:
            total_price+=item.price
        return total_price



