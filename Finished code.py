import random
import string
class Customer:
    def __init__(self, cusname="", cusaddress="", mobilenum=""):
        self.CustomerName = cusname
        self.CustomerAddress = cusaddress
        self.Mobilenumber = mobilenum
        self.purchase_orders = []


    ##################
    def getCustomerName(self):
        return self.CustomerName

    def setCustomerName(self, CustomerName):
        self.CustomerName = CustomerName

    def getCustomerAddress(self):
        return self.CustomerAddress

    def setCustomerAddress(self, CustomerAddress):
        self.CustomerAddress = CustomerAddress

    def getMobilenumber(self):
        return self.Mobilenumber

    def setMobilenumber(self, Mobilenumber):
        self.Mobilenumber = Mobilenumber

    def __str__(self):
        return "Name: {}\nAddress: {}\nPhone number: {}".format(self.getCustomerName(), self.getCustomerAddress(), self.getMobilenumber())
    ##################


class MobileApp:
    def __init__(self):
        self.selected_items = []
        self.current_machine = None
        self.customer = self.get_customer_information()

    def get_selected_items(self):
        return self.selected_items

    def set_selected_items(self, items):
        self.selected_items = items

    def get_current_machine(self):
        return self.current_machine

    def set_current_machine(self, machine):
        self.current_machine = machine

    def generate_alphanumeric_key(self, length):
        characters = string.ascii_letters + string.digits
        random_key = ''.join(random.choice(characters) for i in range(length))
        return random_key

    def get_customer_information(self):
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        mobile_number = input("Enter your mobile number: ")

        customer = Customer(name, address, mobile_number)
        return customer


    #function to start selecting and paying for items
    def select_items(self, vending_machine):
        #Welcomes users to vending machines and asks for vending machine ID
        machine_id = input("HELLO! Welcome to Our SMART VendingMachine. To Proceed \nEnter The Vending Machine ID: ")
        selected_machine = None
        #Checks if the Vending machine is avaiable
        for machine in vending_machine:
            if machine.machine_id == machine_id:
                selected_machine = machine
                break
        #shows the items to the user
        if selected_machine:
            selected_machine.get_items()
            total_cost = 0
            #asks the user to put the ID of the selected item
            while True:
                item_id = input("Enter the item ID to select the item you want (or 'done' to finish): ")

                if item_id.lower() == 'done':
                    if total_cost == 0:
                        print("Transaction Canceled. No items Selected")
                    else:
                        print(f"Total Cost: ${total_cost}")
                        confirm = input("Would you like to proceed with the payment? (yes/no): ").lower()
                        if confirm == "yes":
                            random_key = self.generate_alphanumeric_key(10)
                            print(f"Your Item key code is {random_key}. Please Do NOT Share It")
                            code = input("Input Your Item Code Please : ")
                            if code == random_key:
                                for selected_item in self.selected_items:
                                    selected_item.update_item_quantity(selected_item.purchase_quantity)
                                selected_machine.update_total_sales(total_cost)
                                print(f"Payment successful.\nEmjoy your Food!\nThank you for using SMART VendingMachine!")
                                self.selected_items.clear()
                            else:
                                print("Wrong key")
                        else:
                            print("Payment cancelled")
                    break

                selected_item = selected_machine.find_item_by_id(item_id)
                # emplemented a try and except to deal with the error that comes from putting a letter instead of a number
                if selected_item:
                    try:
                        quantity_to_purchase = int(input(f"How many {selected_item.item_name} would you like to purchase? "))
                        if quantity_to_purchase <= selected_item.quantity:
                            selected_item.purchase_quantity = quantity_to_purchase
                            self.selected_items.append(selected_item)
                            print(f"{quantity_to_purchase} {selected_item.item_name}(s) added to your order.")
                            total_cost += selected_item.price * quantity_to_purchase
                        else:
                            print(f"Not enough {selected_item.item_name} in stock.")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print(f"Item with ID {item_id} not found.")


class VendingMachine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.items = []
        self.total_sales = 0

    def __str__(self):
        return f"VendingMachine ID: {self.machine_id}, Total Sales: {self.total_sales}"


    ##################

    def get_machine_id(self):
        return self.machine_id

    def set_machine_id(self, new_id):
        self.machine_id = new_id

    def set_items(self, items_list):
        self.items = items_list

    def get_total_sales(self):
        return self.total_sales

    def set_total_sales(self, new_total):
        self.total_sales = new_total

    def get_items(self):
        print("Items available in Vending Machine " + self.machine_id + ":")
        print("ID   Item Name               Price   Quantity   Type")
        print("--------------------------------------------------")
        for item in self.items:
            print(f"{item.item_id}   {item.item_name:<23} ${item.price:<7} {item.quantity}         {item.Type}")

    ##################

    def add_item(self, item):
        self.items.append(item)

    def find_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def update_total_sales(self, total_cost):
        self.total_sales += total_cost

    def get_total_sales(self):
        print(f"The total sales in Vending Machine {self.machine_id} is: {self.total_sales}")

    def display_sales_by_type(self):
        sweet_sales, salty_sales, liquid_sales = 0, 0, 0
        for item in self.items:
            if isinstance(item, Sweet):
                sweet_sales += item.get_sales_count()
            elif isinstance(item, Salty):
                salty_sales += item.get_sales_count()
            elif isinstance(item, Liquid):
                liquid_sales += item.get_sales_count()
        print(f"Sweet items sold: {sweet_sales}")
        print(f"Salty items sold: {salty_sales}")
        print(f"Liquid items sold: {liquid_sales}")


    def display_machine_sales_summary(self):
        print(f"\nSales Summary for Vending Machine {self.machine_id}:")
        print("-" * 50)  # Divier line
        print(f"{'Item':<20} | {'Total Sold':<10} | {'Total Sales':<10}")
        print("-" * 50)  # Divider line

        total_sales = 0
        for item in self.items:
            item_sales = item.price * item.get_sales_count()
            total_sales += item_sales
            print(f"{item.item_name:<20} | {item.get_sales_count():<10} | ${item_sales:<10.2f}")

        print("-" * 50)  # divider line
        print(f"{'Total Sales':<20} | {' ':<10} | ${total_sales:<10.2f}")
        print("-" * 50)  # Divder line



    def display_all_machines_sales(vending_machines):
        for machine in vending_machines:
            machine.display_machine_sales_summary()

class Item:
    def __init__(self, item_id, item_name, manufacturer, price, quantity, item_type):
        self.item_id = item_id
        self.item_name = item_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
        self.Type = item_type
        self.sales_count = 0
        self.purchase_quantity = 0  # This will keep track of the quantity of the item being purchased.

    def __str__(self):
        return (f"Item ID: {self.item_id}, Name: {self.item_name}, Manufacturer: {self.manufacturer}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Type: {self.Type}")


    ##################

    def get_item_id(self):
        return self.item_id

    def set_item_id(self, new_id):
        self.item_id = new_id

    def get_item_name(self):
        return self.item_name

    def set_item_name(self, new_name):
        self.item_name = new_name

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_type(self):
        return self.Type

    def set_type(self, new_type):
        self.Type = new_type

    def get_sales_count(self):
        return self.sales_count

    def set_sales_count(self, new_count):
        self.sales_count = new_count

    def get_purchase_quantity(self):
        return self.purchase_quantity

    def set_purchase_quantity(self, quantity):
        self.purchase_quantity = quantity

    ##################

    def update_item_quantity(self, quantity_sold):
        self.quantity -= quantity_sold
        self.sales_count += quantity_sold








class Sweet(Item):
    def __init__(self, item_id, item_name, manufacturer, price, quantity, item_type, flavor, sugar_content, is_sugar_free):
        super().__init__(item_id, item_name, manufacturer, price, quantity, item_type)
        self.flavor = flavor
        self.sugar_content = sugar_content
        self.is_sugar_free = is_sugar_free

    def __str__(self):
        return (f"Sweet - {super().__str__()}, Flavor: {self.flavor}, "  #calls the __str__ method of the superclass item
                f"Sugar Content: {self.sugar_content}g, Sugar Free: {self.is_sugar_free}")

    def display_sales(self):
        print(f"Sweet items sold: {self.item_name} items sold: {self.get_sales_count()}")


    ##################
    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_sugar_content(self):
        return self.sugar_content

    def set_sugar_content(self, sugar_content):
        self.sugar_content = sugar_content

    def get_is_sugar_free(self):
        return self.is_sugar_free

    def set_is_sugar_free(self, is_sugar_free):
        self.is_sugar_free = is_sugar_free
    ##################


class Salty(Item):
    def __init__(self, item_id, item_name, manufacturer, price, quantity, item_type, salt_content, is_spicy, seasoning):
        super().__init__(item_id, item_name, manufacturer, price, quantity, item_type)
        self.salt_content = salt_content
        self.is_spicy = is_spicy
        self.seasoning = seasoning

    def __str__(self):
        return (f"Salty - {super().__str__()}, Salt Content: {self.salt_content}g, "
                f"Spicy: {self.is_spicy}, Seasoning: {self.seasoning}")

    def display_sales(self):
        print(f"Salty items: {self.item_name} items sold: {self.get_sales_count()}")


    ##################

    def get_salt_content(self):
        return self.salt_content

    def set_salt_content(self, salt_content):
        self.salt_content = salt_content

    def get_is_spicy(self):
        return self.is_spicy

    def set_is_spicy(self, is_spicy):
        self.is_spicy = is_spicy

    def get_seasoning(self):
        return self.seasoning

    def set_seasoning(self, seasoning):
        self.seasoning = seasoning
    ##################


class Liquid(Item):
    def __init__(self, item_id, item_name, manufacturer, price, quantity, item_type, volume, container_type, is_carbonated):
        super().__init__(item_id, item_name, manufacturer, price, quantity, item_type)
        self.volume = volume
        self.container_type = container_type
        self.is_carbonated = is_carbonated

    ##################

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_container_type(self):
        return self.container_type

    def set_container_type(self, container_type):
        self.container_type = container_type

    def get_is_carbonated(self):
        return self.is_carbonated

    def set_is_carbonated(self, is_carbonated):
        self.is_carbonated = is_carbonated
        
    ##################

    def __str__(self):
        return (f"Liquid - {super().__str__()}, Volume: {self.volume}ml, "
                f"Container: {self.container_type}, Carbonated: {self.is_carbonated}")


    def display_sales(self):
        print(f"liquid item: {self.item_name} items sold: {self.get_sales_count()}")





# Example usage:
vending_machine1 = VendingMachine("VM001")
vending_machine2 = VendingMachine("VM002")

#grouping the vending machines
vending_machines = [vending_machine1, vending_machine2]  # Add as many as you have


Sweet_item1 = Sweet("001", "Strawberry gum", "Starburst", 1.5, 50, "Sweet", "Strawberry", 10, False)
Sweet_item2 = Sweet("004", "Chocolate Bar", "Cadbury", 1.8, 40, "Sweet", "Chocolate", 15, False)
Sweet_item3 = Sweet("005", "Fruit Jelly", "Jelly Belly", 2.5, 35, "Sweet", "Assorted Fruits", 20, False)
Sweet_item4 = Sweet("006", "Mint Candy", "Mentos", 1.2, 60, "Sweet", "Mint", 5, True)

# Additional Salty items
Salty_item1 = Salty("002", "Salt & Vinegar Chips", "Lays", 2.0, 30, "Salty", 5, False, "Salt & Vinegar")
Salty_item2 = Salty("007", "BBQ Potato Chips", "Pringles", 2.5, 25, "Salty", 6, False, "BBQ")
Salty_item3 = Salty("008", "Pretzels", "Snyder's", 1.7, 40, "Salty", 4, False, "Original")

# Additional Liquid items
Liquid_item1 = Liquid("003", "Pepsi", "PepsiCO", 1.0, 25, "Liquid", 330, "Can", True)
Liquid_item2 = Liquid("009", "Orange Juice", "Tropicana", 2.0, 30, "Liquid", 250, "Bottle", False)
Liquid_item3 = Liquid("010", "Mineral Water", "Aquafina", 1.5, 50, "Liquid", 500, "Bottle", False)



vending_machine1.add_item(Sweet_item1)
vending_machine1.add_item(Sweet_item2)
vending_machine1.add_item(Salty_item1)
vending_machine1.add_item(Liquid_item2)
vending_machine1.add_item(Liquid_item3)



vending_machine2.add_item(Sweet_item3)
vending_machine2.add_item(Sweet_item4)
vending_machine2.add_item(Salty_item2)
vending_machine2.add_item(Salty_item3)
vending_machine2.add_item(Liquid_item1)


print("Available SMART Vending Machines:\n VM001\n VM002")

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Initiating a Test Run of the Item Purchase Procedure")
app = MobileApp()
app.select_items([vending_machine1, vending_machine2])

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Displaying sales: \n")

#to loop through all the vending machines Available
salesinput = input("Do you want to proceed with checking sales for ALL vending machines? (yes/no): ").lower()
if salesinput == "yes":
    for machine in vending_machines:
        machine.display_machine_sales_summary()
else:
    print("done")
