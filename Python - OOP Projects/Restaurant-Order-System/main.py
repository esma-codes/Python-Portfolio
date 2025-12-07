from menu import Food,Drink
from table import Table

def Menu():

    Menu=[ Food("F-001","Dark Burger",125,"Main Dish"),
           Food("F-002", "Butcher Burger", 135.50, "Main Dish"),
           Food("F-003", "Anatolian Burger", 120, "Main Dish"),
           Food("F-004", "Chicken Burger", 110.50, "Main Dish"),
           Food("F-101", "Pie", 100, "Dessert"),
           Food("F-102", "chocolate bomb", 135.50, "Dessert"),
           Drink("D-111","Cola",50,"100 ml"),
           Drink("D-112", "Ayran", 50, "75 ml"),
           Drink("D-113", "Lemonade", 50, "90ml")

    ]
    return Menu
def print_menu():
    print("\n--- Restaurant Menu ---")
    print("1. View All Products (Menu)")
    print("2. Add item to order")
    print("3. Remove item from order")
    print("4. View Your order")
    print("0. Exit ")

def main():
    restaurant_menu = Menu()
    number_table=int(input("Enter your table number: "))
    current_table=Table(number_table)
    while True:
        print_menu()
        choice=input("Choose an operation:  ").strip().lower()

        if choice=="1":
            for item in restaurant_menu:
                print(item)
        elif choice=="2":
            id_to_find=input("Enter Item ID: ")
            found_item_object = None
            for item in restaurant_menu:
                if item.item_id==id_to_find:
                    found_item_object=item
                    break
            if found_item_object:
                current_table.add_to_order(found_item_object)
                print(f"SUCCESS: {found_item_object.name} added to order.")
            else:
                print(f"ERROR: Item with ID '{id_to_find}' not found in menu.")


        elif choice=="3":
            id_to_find = input("Enter Item ID: ")
            found_item_object = None
            for item in restaurant_menu:
                if item.item_id == id_to_find:
                    found_item_object=item
                    break
            if found_item_object:
                current_table.remove_to_order(found_item_object)
                print(f"SUCCESS: {found_item_object.name} deleted to order.")
            else:
                print(f"ERROR: Item with ID '{id_to_find}' not found in menu.")

        elif choice=="4":
            current_table.view_to_order()

        elif choice=="0":
            print("********Exit********")
            return
        else:
            print("Invalid choice!")


if __name__=="__main__":
    main()












