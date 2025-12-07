class MenuItem:
    def __init__(self,id,name,price):
        self.item_id=id
        self.name=name
        self.price=price

    def __str__(self):
        return f" ID:{self.item_id:<8} |Name:{self.name:<25} |Price: {self.price:<10.2f}"

class Food(MenuItem):
    def __init__(self,id,name,price,category):
        super().__init__(id,name,price)
        self.category=category

    def __str__(self):
        base_str=super().__str__()
        return f"[FOOD] {base_str} | Food Category:{self.category}"

class Drink(MenuItem):
    def __init__(self,id,name,price,size_ml):
        super().__init__(id,name,price)
        self.size_ml=size_ml

    def __str__(self):
        base_str=super().__str__()
        return f"[DRINK] {base_str} | Drink Size: {self.size_ml}"



