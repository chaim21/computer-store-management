from display import show_invetory_menu , show_one_product
from products import show_all_products
from data import products
from helpers import get_input
from validations import positive_num

def show_all_products(products:list):
    for product in products:
        if product["active"] == True and product["stock"] > 0:
            show_one_product(product)

def search_active_product_by_id(products):
    id = get_input("enter id:\n",positive_num)
    prodact_id = int(id)
    for p in products:
        if p["id"] == prodact_id:
            if p["active"] == True:
                return p
            else:
                print("product not active!!")

def run_inventory_menu():
    choice = False
    while not choice:
        show_invetory_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                show_all_products(products)
            case "2":
                product = search_active_product_by_id(products)
                print("not found") if not product else show_one_product(product)