from display import show_invetory_menu , show_one_product
from products import show_all_products
from data import products
from helpers import get_input
from validations import positive_num

#show_all_active_products
def show_all_active_products(products:list):
    for product in products:
        if product["active"] == True and product["stock"] > 0:
            show_one_product(product)

#search_active_product_by_id
def search_active_product_by_id(products):
    id = get_input("enter id:\n",positive_num)
    prodact_id = int(id)
    for p in products:
        if p["id"] == prodact_id:
            if p["active"] == True:
                return p
            else:
                print("product not active!!")

#Add units to inventory
def add_units_to_inventory(prodacts):
    id = get_input("enter id:\n",positive_num)
    prodact_id = int(id)
    quantity = get_input("Enter quantity to add:\n",positive_num)
    for p in products:
        if p["id"] == prodact_id:
                show_one_product(p)
                p["stock"] += int(quantity)
                show_one_product(p)
                return True

#Deduct units from inventory
def dedcut_units_from_inventory(products):
    id = get_input("enter id:\n",positive_num)
    prodact_id = int(id)
    quantity = get_input("Enter quantity to reduce:\n",positive_num)
    for p in products:
        if p["id"] == prodact_id:
            if p["stock"] - int(quantity) < 0:
                print("Inventory cannot be reduced below zero.")
                return True
            else:
                show_one_product(p)
                p["stock"] -= int(quantity)
                show_one_product(p)
                return True

#View out-of-stock products
def show_out_of_stock_products(products):
    for product in products:
        if product["stock"] > 0:
            show_one_product(product)

#View products with low stock
def show_products_with_low_stock(products):
    low_stock = 5
    for product in products:
        if product["stock"] <= low_stock:
            show_one_product(product)

def run_inventory_menu():
    wanna_exit = False
    while not wanna_exit:
        show_invetory_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                show_all_products(products)
            case "2":
                product = search_active_product_by_id(products)
                print("not found") if not product else show_one_product(product)
            case "3":
                add_product = add_units_to_inventory(products)
                print("Added successfully") if add_product else print("not found!!")
            case "4":
                sub_product = dedcut_units_from_inventory(products)
                print("sub successfully") if sub_product else print("not found!!")
            case "5":
                show_out_of_stock_products(products)
            case "6":
                show_products_with_low_stock(products)
            case "7":
                wanna_exit = True
            case _:
                print("invalid choice!!")

