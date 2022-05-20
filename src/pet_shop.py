def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount_to_add):
    pet_shop["admin"]["total_cash"] += amount_to_add

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]