from order import Order

class Table:
    def __init__(self,table_number):
        self.table_number=table_number
        self.order=Order()

    def add_to_order(self,order):
        self.order.add_item(order)
        print(f"{order.name}  added in the table.")

    def remove_to_order(self,order):
        self.order.remove_item(order)
        print(f"{order.name} deleted in the table.")

    def view_to_order(self):
        print(f"----{self.table_number}'s Order----")
        self.order.list_items()
        total=self.order.calculate_items()
        print(f"----------------------------")
        print(f"TOTAl PRICE:{total:.2f} TL")
        return total






