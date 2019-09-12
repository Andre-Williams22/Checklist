from colorama import Fore
checklist = list()
 #create
def create(item):
	checklist.append(item)

# Read
def read(index):
	print(checklist[index])
	return checklist[index]

# Update
def update(index, item):
	checklist[index] = item
# destroy
def destroy(index):
	checklist.pop(index)

def list_all_items():
	index = 0
	for list_item in checklist:
		print("{} {}".format(index, list_item))
		#print(str(index) + list_item)
		index += 1
def select(function_code):
	#Create Item
	if function_code == 'C':
		input_item = user_input('Input_item: ')
		create(input_item)
	#Read Item
	elif function_code == 'R':
		item_index = int(user_input('Index Number?'))
		# Remember that item_index must actually exist or our program will crash.
		read(item_index)

	#Print all items
	elif function_code == 'P':
		list_all_items()

	elif function_code == 'Q':
		return False
	#catch everything
	else:
		print('Unkown')
	return True

def user_input(prompt):
	user_value = input(prompt)
	return (user_value)

'''
def test():
	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	select('C')
	list_all_items()

	select('R')
	list_all_items()
	#continues until all code is run
	list_all_items()
test()
'''
running = True
while running:
    selection = user_input(
        "Press C to add to list, " + Fore.BLUE + " R to Read from list, " + Fore.RESET + " P to display list, and Q to quit")
    running = select(selection)