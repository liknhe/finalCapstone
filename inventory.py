#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes.
    
    You must use the try-except in this function for error handling. 
    
    Remember to skip the first line using your code.
    '''
        

        # Read lines except for heading
        
    while True:
            try: 
                inventory = open('inventory.txt', 'r')

                lines = inventory.readlines()
                for i in range(1, len(lines)):
                    record = lines[i].split(",")
                    shoe = Shoe(record[0],record[1],record[2],record[3],record[4])
                    shoe_list.append(shoe)

                break
            except FileNotFoundError as error:
                print(error)
                print("The file that you are trying to open does not exist. Try again..")
            finally:
                if inventory is not None:
                    inventory.close()

            

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Please enter the shoe's country of origin: ")
    code = input("Please enter the shoe's code: ")
    product = input("Please enter the shoe name: ")
    cost = int(input("Please enter the shoe's cost: "))
    quantity = int(input("Please enter the shoe stock: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. 
    Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    for shoe in shoe_list:
        print(shoe)

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    shoe = shoe_list[0]
    lowest_stock = shoe.get_quantity()

    for x in shoe_list:
        if x.get_quantity() < lowest_stock:
            shoe = x

    print(f"\nShoe: {shoe.product}, stock remaining: {shoe.get_quantity()}")

    to_restock = input("Would you like to restock? (Y/N): ")
    if to_restock.lower() == "y":
        restock_amount = int(input("How many pairs of shoe to restock:"))
        shoe.quantity = int(shoe.get_quantity()) + restock_amount

    print(f"\nShoe: {shoe.product}, stock remaining: {shoe.get_quantity()}")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Please enter the shoe code to begin search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        print(shoe)
        print(f"Total value: {int(shoe.get_quantity()) * int(shoe.get_cost())}\n")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe = shoe_list[0]
    biggest_stock = shoe.get_quantity()

    for x in shoe_list:
        if x.get_quantity() > biggest_stock:
            shoe = x

    print("The following shoe is on sale: ")
    print(shoe)
  
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()

action = input('''Enter your action: 
as - add shoe
va - view all
re - restock
ss - search shoe
vpi - value per item
sale - identify the shoe with the most inventory
quit - exit
''')

while action.lower != "quit":

    if action.lower() == "as":
        capture_shoes()
    elif action.lower() == "va":
        view_all()
    elif action.lower() == "re":
        re_stock
    elif action.lower() == "ss":
        search_shoe()
    elif action.lower() == "vpi":
        value_per_item()
    elif action.lower() == "sale":
        highest_qty
    
    action = input('''\nEnter your action: 
as - add shoe
va - view all
re - restock
ss - search shoe
vpi - value per item
sale - identify the shoe with the most inventory
quit - exit
''')

