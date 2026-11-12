def is_empty(txt):
    if txt.strip():
        return True,None
    return False ,"cannot exepet empty value"

def positive_num(n):
    try:
        num = int(n)
        if num > 0:
            return True ,None
    except ValueError:
        return False , "must be a positive number"

def valid_category(category,categories):
    if category.capitalize() in categories:
        return True , None
    return False , "category not exsits"

