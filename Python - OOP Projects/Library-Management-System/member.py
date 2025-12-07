class Member:
    def __init__(self, name, member_ide):
        self.name = name
        self.member_ide = member_ide
        self.borrowed_items = []



    def __str__(self):
        item_count = len(self.borrowed_items)
        return f"Member name:{self.name}-Member ID:{self.member_ide}-Number of books: {item_count}"

