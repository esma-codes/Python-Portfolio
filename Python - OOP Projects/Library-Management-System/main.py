from library import Library

def print_menu():
    print("\n--- Library Management System v2.0 ---")
    print("1. Add New Book")
    print("2. Add New Magazine")
    print("3. Add New DVD")
    print("4. Add New Member")
    print("5. Lend Item")
    print("6. Return Item")
    print("7. List All Items in Library")
    print("8. List All Members")
    print("0. Exit Application")


def main():
    my_library = Library()

    print("Welcome to the Library Management System!")

    while True:
        print_menu()
        choice = input("\nEnter your choice (0-8): ")

        if choice == '1':
            my_library.add_book()

        elif choice == '2':
            my_library.add_magazine()

        elif choice == '3':
            my_library.add_dvd()

        elif choice == '4':
            my_library.add_member()

        elif choice == '5':
            my_library.lend_item()

        elif choice == '6':
            my_library.return_item()

        elif choice == '7':
            print("\n--- Listing All Library Items ---")
            if not my_library.all_items:
                print("There are no items in the library yet.")
            else:
                for item in my_library.all_items:
                    print(item)

        elif choice == '8':
            print("\n--- Listing All Members ---")
            if not my_library.all_members:
                print("There are no members registered yet.")
            else:
                for member in my_library.all_members:
                    print(member)

        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 8.")


if __name__ == "__main__":
    main()