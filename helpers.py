from validations import is_empty , positive_num , valid_category
from data import categories
def get_input(msg,validation,*kwargs):
    valid_input = False
    while not valid_input:
        input_value = input(msg)
        valid_input , error_msg = validation(input_value,*kwargs)
        if not valid_input:
            print(error_msg)
    return input_value

def valid_new_product():
    name = get_input("enter product name:\n",is_empty)
    category = get_input("enter product category:\n",valid_category,categories).capitalize()
    price = get_input("enter product price:\n",positive_num)
    price = int(price)
    stock = get_input("enter inventory quantity:\n",positive_num)
    stock = float(stock)
    return name,category,price,stock
    