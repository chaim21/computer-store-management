from display import show_products_managment_menu , show_one_product
from helpers import valid_new_product , get_input
from data import products , categories
from validations import is_empty , positive_num

#add new product
def add_product(products:list):
    name , category , price , stock = valid_new_product()
    new_id = generate_id(products)
    new_item ={"id": new_id, "name":name, "category":category, "price":price, "stock":stock, "active": True}
    products.append(new_item)
    return new_item
    
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
    for n in products:
        if n["name"][:len(name)].lower() == name.lower():
            return n

def search_by_category(category,products):
    found = []
    for c in products:
        if c["category"].lower() == category.lower():
            found.append(c)
    return found

def search_product():
    found = False
    while not found:
        choice = input("1: search by id\n2: search by name \n3: search by category\n4: EXIT\nchoose:\n")
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

#update prodact
def update_product():
    id = get_input("enter id of product:\n",positive_num)
    found = search_by_id(int(id),products)
    if not found:
        print( "id product not exists!!")
        return False
    show_one_product(found)
    change = get_input("what do you want to change: (name/categoey/price/active):\n",is_empty)
    if change.lower() == "name":
        new_name = get_input("enter new name:\n",is_empty)
        found["name"] = new_name
        show_one_product(found)
        return True
    elif change.lower() == "category":
        new_category = get_input("enter new category:\n",is_empty)
        if search_by_category(new_category,categories):
            found["category"] = new_category
            show_one_product(found)
            return True
    elif change.lower() == "price":
        new_price = get_input("enter new price\n",positive_num)
        found["price"] = float(new_price)
        show_one_product(found)
        return True
    elif change.lower() == "active":
        found["active"] = not found["active"]
        
        show_one_product(found)
        return True
    else:
        print("invalid choice!!\n")
        return False

#delete prodact
def delete_product(products:list):
    id = get_input("enter id of product to delete:\n",positive_num)
    found = search_by_id(int(id),products)
    if not found:
        return "not found!!"
    show_one_product(found)
    choice = get_input("Are you sure you want to delete? enter (Y/N)\n",is_empty)
    if choice.lower() == "y":
        products.remove(found)
        return ("Successfully deleted")
    elif choice.lower() == "n":
        return("Cancelled")
    else:
        return("invalid choice!!")

def run_products_managment_menu():
    wanna_exit = False
    while not wanna_exit:
        show_products_managment_menu()
        choice = input("Choose an option:\n")
        match choice:
            case "1":
                new_item = add_product(products)
                show_one_product(new_item)
                print("Added successfully")
            case "2":
                show_all_products(products)
            case "3":
                search_product()
            case "4":
                if update_product():
                    print("Updated successfully")
            case "5":
                print(delete_product(products))
            case "6":
                wanna_exit = True
            case _:
                print("invalid choice")