

def show_main_menu():
    print('''
================================= 
       COMPUTER STORE SYSTEM 
================================= 
 
1. Products Management 
2. Inventory Management 
3. Sales Management 
4. Reports 
5. Exit 
''')

def show_products_managment_menu():
    print('''
--------- PRODUCTS MANAGEMENT --------- 
 
1. Add Product 
2. Display All Products 
3. Search Product 
4. Update Product 
5. Delete Product 
6. Back to Main Menu 

''')

def show_one_product(p:dict):
    print(f'''
id: {p["id"]} - name: {p["name"]} - category: {p["category"]} - price: {p["price"]} - stock: {p["stock"]} - active: {p["active"]}''')
