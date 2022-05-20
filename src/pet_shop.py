def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount_to_add):
    pet_shop["admin"]["total_cash"] += amount_to_add

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_of_pets_sold):
    pet_shop["admin"]["pets_sold"] += number_of_pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_of_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_of_breed.append(pet)
    return pets_of_breed

def find_pet_by_name(pet_shop, pet_name):
    # return dictionary for found pet
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer_id):
    return customer_id["cash"]

