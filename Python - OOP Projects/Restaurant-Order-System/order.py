from menu import MenuItem

class Order:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)


    def remove_item(self,item):
        self.items.remove(item)


    def list_items(self):
        if not self.items:
            print("Your order is empty.")
        else:
            for item in self.items:
                print(item)

    def calculate_items(self):
        total_price=0
        for item in self.items:
            total_price+=item.price
        return total_price


