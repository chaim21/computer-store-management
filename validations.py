def is_empty(txt):
    if txt.strip():
        return True,None
    return False ,"cannot exepet empty value"

def positive_num(n):
    try:
        num = int(n)
        if num >= 0:
            return True ,None
        return False , "must be a positive integer"
    except ValueError:
        return False , "must be a positive integer"

def valid_category(category,categories):
    if category.capitalize() in categories:
        return True , None
    return False , "category not exsits"

def positive_float(n):
    try:
        num = float(n)
        if num > 0:
            return True, None
        return False, "must be a positive number"
    except ValueError:
        return False, "must be a positive number"