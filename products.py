from display import show_products_managment_menu , show_one_product
from helpers import valid_new_product , get_input
from data import products
from validations import is_empty , positive_num
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

# Search Product with id/name/category
def search_by_id(id,products):
    for p in products:
        if p["id"] == id:
            return p

def search_by_name(name,products):
    for n in name:
        if n["name"][:len(name)].lower() == name.lower():
            return name

def search_by_category(category,products):
    found = []
    for c in products:
        if c["category"].lower() == category.lower():
            found.append(c)
    return found

def search_product():
    found = False
    while not found:
        choice = input("1: search by id\n2: search by name \n1: search by category\n4: EXIT\nchoose:\n")
        match choice:
            case "1":
                id = get_input("enter id:\n",positive_num)
                prodact = search_by_id(int(id),products)
                print("not found") if not prodact else show_one_product(prodact)
            case "2":
                name = get_input("enter name:\n",is_empty)
                prodact = search_by_name(name,products)
                print("not found") if not prodact else show_one_product(prodact)
            case "3":
                category = get_input("enter category:\n",is_empty)
                prodact = search_by_category(category,products)
                print("not found") if not prodact else show_all_products(prodact)
            case "4":
                found = True
            case _:
                print("enter num between (1-3)")

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
            case "3":
                search_product()