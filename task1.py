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
			

def update_stock(store_dict, name, quantity):
	if name in store_dict:
		store_dict[name] = {'quantity': quantity}
		return f'PRODUCT {name} UPDATED SUCCESSFUL!'
	else:
		return f'PRODUCT DON"T EXIST!'


def sell_product(store_dict, name, quantity):
	if name not in store_dict:
		return f'PRODUCT {name} NOT IN STORE!'
	elif store_dict[name]['quantity'] < quantity:
		return f'NO ENOGH PRODUCT OF {name} IN STORE'
	else:
		store_dict[name]['quantity'] -= quantity
		total_price = store_dict[name]['price'] * quantity
		return f'{quantity} of {name} sold for ${total_price}'

def display_inventory(store_dict):
	for product, details in store_dict.items():
		print(f'{product} Price: ${details["price"]}, Quantity: {details["quantity"]}')


#def most_expensive_product(store_dict):
	




def total_potential_sales(store_dict):
	total = sum(details['price'] * details['quantity'] for details in store_dict.values())
	return f'Total potentail sales (if everything is sold): ${total}'

def start():
	print('Welcome to online Store Inventory & Sales System')
	while True:
		print('''
		OPTIONS:
		1. Add a new product.
		2. Update product.
		3. Sell product.
		4. View invention.
		5. Most expensive product.
		6. Total potential sales.
		7. Exit
		''')

		option = int(input('Enter option:\n>>'))
		if option == 1:
			name = input('Enter name:\n>>')
			price = float(input('Enter price:\n>>'))
			quantity = int(input('Enter quantity:\n>>'))
			print(add_product(store, name, price, quantity))
		elif option == 2:
			name = input('Enter name:\n>>')
			quantity = int(input('Enter quantity:\n>>'))
			print(update_stock(store, name, quantity))
		elif option == 3:
			name = input('Enter name:\n>>')
			quantity = int(input('Enter quantity:\n>>'))
			print(sell_product(store, name, quantity))
		elif option == 4:
			display_inventory(store)
		elif option == 5:
			print('most_expensive_product(store)')
		elif option == 6:
			print(total_potential_sales(store))
		elif option == 7:
			print('EXITING......\nGOODBYE!')
			break
		else:
			print('INVALID OPTION..\nTRY AGAIN!.')



start()
