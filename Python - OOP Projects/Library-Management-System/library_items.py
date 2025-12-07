class LibraryItem:
    def __init__(self,title,isbn):
        self.title = title.capitalize()
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "On Loan"
        return f"{self.title:<30} | ISBN: {self.isbn:<15} | Status: {status}"


class Book(LibraryItem):
    def __init__(self,title,isbn,author):
        super().__init__(title,isbn)
        self.author = author.capitalize()
    def __str__(self):
        base_str=super().__str__()
        return f"[BOOK] {base_str} | Author: {self.author}"

class Magazine(LibraryItem):
    def __init__(self,title,isbn,issue_number):
        super().__init__(title,isbn)
        self.issue_number = issue_number

    def __str__(self):
        base_str = super().__str__()
        return f"[MAG]   {base_str} | Issue: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self,title,isbn,director):
        super().__init__(title,isbn)
        self.director = director.capitalize()

    def __str__(self):
        base_str = super().__str__()
        return f"[DVD]   {base_str} | Director: {self.director}"





