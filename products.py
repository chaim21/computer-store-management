from display import show_products_managment_menu , show_one_product
from helpers import valid_new_product
from data import products

#add new product
def add_product(products:list):
    name , category , price , stock = valid_new_product()
    new_id = generate_id(products)
    new_item ={"id": new_id, "name":name, "category":category, "price":price, "stock":stock, "active": True},
    products.append(new_item)
    
def generate_id(products:list):
    return max([product["id"] for product in products]) + 1

#display All active Products
def show_all_products(products:list):
    for product in products:
        if product["active"] == True:
            show_one_product(product)



def run_products_managment_menu():
    choice = None
    while choice != "6":
        show_products_managment_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                add_product(products)
            case "2":
                show_all_products(products)