class Product:
    def __init__(self,id,name,price):
        self.product_ide=id
        self.name=name
        self.price=price

    def __str__(self):
        return f" Product's Name:{self.name} | Product's Price:{self.price} | Product's IDE:{self.product_ide} "

class Electronics(Product):
    def __init__(self,id,name,price,warranty):
        super().__init__(id,name,price)
        self.warranty_period=warranty

    def __str__(self):
        base_str=super().__str__()
        return f"[ELECTRONICS] {base_str} |Product's Warranty:{self.warranty_period}"

class Clothing(Product):
    def __init__(self,id,name,price,size,color):
        super().__init__(id,name,price)
        self.size=size
        self.color=color

    def __str__(self):
        super().__str__()
        return f"Product's Size:{self.size} | Product's Color:{self.color}"

class Book(Product):
    def __init__(self,id,name,price,author):
        super().__init__(id,name,price)
        self.author=author

    def __str__(self):
        base_str=super().__str__()
        return f"[CLOTHING] {base_str} |Product's Author:{self.author}"




