from display import show_main_menu 
import products
import inventory

def run_main_menu():
    choice = None
    while choice != "5":
        show_main_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                products.run_products_managment_menu()
            case "2":
                inventory.run_inventory_menu()

run_main_menu()
