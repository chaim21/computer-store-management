from display import show_products_managment_menu
from helpers import valid_new_product
from data import products

def add_product(products:list):
    name , category , price , stock = valid_new_product()
    new_id = generate_id(products)
    new_item ={"id": new_id, "name":name, "category":category, "price":price, "stock":stock, "active": True},
    products.append(new_item)
    

def generate_id(products:list):
    return max([product["id"] for product in products]) + 1


def run_products_managment_menu():
    choice = None
    while choice != "6":
        show_products_managment_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                add_product(products)