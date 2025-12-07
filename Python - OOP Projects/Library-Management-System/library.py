from member import Member
from library_items import Book,Magazine,DVD

class Library:
    def __init__(self):
        self.all_items=[]
        self.all_members=[]

    def add_member(self):
        name=str(input("Enter your name: ")).capitalize()
        ide=int(input("Enter your ID number: "))
        new_member=Member(name,ide)
        self.all_members.append(new_member)
        print(f"{new_member} is added.")



    def remove_member(self):
        ide_to_remove = int(input("Enter your ID number: "))

        for member in self.all_members:
            if member.member_id==ide_to_remove:
                member_to_remove = member
                self.all_members.remove(member_to_remove)
                return
        print(f"No member found with ID {ide_to_remove}.")



    def add_book(self):
        title=str(input("Enter book's title:" )).capitalize()
        author=str(input("Enter book's author:  ")).capitalize()
        isbn=str(input("Enter book's isbn: "))
        new_book=Book(title,author,isbn)
        self.all_items.append(new_book)
        print(f"{new_book} is added.")

    def add_magazine(self):
        title=str(input("Enter magazine's title:" )).capitalize()
        issue_number = str(input("Enter magazine's issue number (e.g., '2025-10'): "))
        isbn=str(input("Enter magazine's isbn: "))
        new_magazine=Magazine(title,isbn,issue_number)
        self.all_items.append(new_magazine)
        print(f"{new_magazine} is added.")

    def add_dvd(self):
        title = str(input("Enter dvd's title:")).capitalize()
        director=str(input("Enter dvd's director: ")).capitalize()
        isbn = str(input("Enter dvd's isbn: "))
        new_dvd = DVD(title, isbn,director)
        self.all_items.append(new_dvd)
        print(f"{new_dvd} is added.")

    def lend_item(self):
        ide_member = int(input("Enter your ID number: "))
        for member in self.all_members:
            if member.member_id==ide_member:
                lend_to_member=member
                break
        if lend_to_member is None:
            print(f"ERROR: {ide_member} ID with member not found.")
            return
        item_isbn=str(input("Please enter isbn of the item  you’d like : "))
        lend_item = None
        for item  in self.all_items:
            if item.isbn==item_isbn:
                lend_item=item
                break

        if lend_item is None:
            print(f"ERROR: {item_isbn} ISBN with item not in library.")
            return

        if not lend_item.is_available:  # lend_book.is_available == False
            print(f"INFO: '{lend_item.title} is currently borrowed by another member.")
            return
        lend_item.is_available = False

        lend_to_member.borrowed_items.append(lend_item)

        print(f"SUCCESSFUL: The item '{lend_item.title}' has been lent to the member named {lend_to_member.name}.")


    def return_item(self):
        ide_member = int(input("Enter your ID number: "))
        for member in self.all_members:
            if member.member_id == ide_member:
                lend_to_member = member
                break
        if lend_to_member is None:
            print(f"ERROR: {ide_member} ID with member not found.")
            return
        item_isbn = str(input("Please enter isbn of the book you’d like : "))

        found_item=None
        for item in self.all_items:
            if item.isbn==item_isbn:
                found_item=item
                break
        if found_item is None:
            print(f"ERROR:{item_isbn} is not registered in library.")
            return
        if found_item not in lend_to_member.borrowed_items:
            print(f"ERROR:{found_item.title} not in {lend_to_member.name}.")
            return
        lend_to_member.borrowed_items.remove(found_item)
        found_item.is_available=True
        print(f"SUCCESS:{found_item} returned to library .")







