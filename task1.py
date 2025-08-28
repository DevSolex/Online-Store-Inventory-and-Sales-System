store = {
	'Labtop': {'price': 1200, 'quantity': 5},
	'Headphones': {'price': 150, 'quantity': 10},
	'Louse': {'price': '40', 'quantity': 20}
	}

def add_product(store_dict, name, price, quantity):
	if name in store_dict:
		return f'PRODUCT {name} ALREADY IN STORE!'
	else:
		store_dict[name] = {'price': price, 'quantity': quantity}
		return f"PRODUCT {name} ADDED SUCCESSFUL!"
			

print(add_product(store, 'name', 500, 2))

def update_stock(store_dict, name, quantity):
	if name in store_dict:
		store_dict[name] = {'quantity': quantity}
		return f'PRODUCT {name} UPDATED SUCCESSFUL!'
	else:
		return f'PRODUCT DON"T EXIST!'
print(update_stock(store, 'name', 3))


