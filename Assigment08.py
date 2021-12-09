# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes by creating product objects to append to a list

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CLi,12.5.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name_str = 'products.txt'
status_str = ''  # optional code debugging string
product_objects_lst = []

class Product(object):
    """Stores data about a product:

    properties:
        name: (string) with the products' name
        price: (float) with the products' standard price
    methods:
        __str__: (string) with product name and price formatted
        to_string: (string) with product name and price formatted
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CLi,12.5.2021,Modified code to complete assignment 8
    """
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    # Properties
    # Property for product name
    @property
    def name(self):
        return str(self.__name).title()
    @name.setter
    def name(self, value):
        if not str(value).isnumeric():
            self.__name = value
        else:
            raise Exception("Product's name cannot be in numbers.")
        if not len(value) == 0:
            self.__name = value
        else:
            raise Exception("Blank entries are not allowed")
    # Property for product price
    @property
    def price(self):
        return float(self.__price)
    @price.setter
    def price(self, value):
        if not str(value).isalpha():
            self.__price = value
        else:
            raise Exception("Product's price must be a number")
        if not len(str(value)) == 0:
            self.__price = value
        else:
            raise Exception("Blank entries are not allowed")
    # Methods
    def __str__(self):
        return self.__name + ", " + str(self.__price)

    def to_string(self):
        return self.__str__()
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_prod_objects): -> a list of product objects

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CLi,12.5.2021,Modified code to complete assignment 8
    """
    # Read data from a file
    @staticmethod
    def read_file_data_to_string(file_name, list_of_prod_obj):
        list_of_prod_obj.clear()  # clear current data
        with open(file_name, 'r') as file:
            for line in file:
                product_object = Product('', 0)
                name, price = line.split(', ')
                product_object.name = name.strip()
                product_object.price = price.strip()
                # print(product_object.to_string())  # testing if each line was converted to an object
                list_of_prod_obj.append(product_object)
            return list_of_prod_obj, 'Success'

    # Save data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_prod_obj):
        with open(file_name, 'w') as file:
            for item in list_of_prod_obj:
                file.write(item.to_string() + '\n')
        return list_of_prod_obj, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects:

    methods:
        print_menu_options(): -> return nothing

        input_menu_choices(): -> string w/ user's menu selection

        print_current_products_in_list(list_of_prod_obj): -> return nothing

        input_products_to_list(product_object, list_of_prod_obj): -> a list of product objects

        input_press_to_continue(optional_message=''): -> optional_message string

    changelog: (When,Who,What)
        CLi,12.5.2021, Wrote functions to allow inputs from user and prints msg to user
    """
    # Shows menu to user
    @staticmethod
    def print_menu_options():
        print('''
              Menu of Options
              0) Exit Program
              1) View current data
              2) Add a new product and its price
              3) Save data and exit
                  ''')
        print()  # Add an extra line for looks

    # Get user's choice
    @staticmethod
    def input_menu_choice():
        choice = str(input('Which option would you like to perform? [0 to 3] - ')).strip()
        print()  # Add an extra line for looks
        return choice

    # Show the current data from the file to user
    @staticmethod
    def print_current_products_in_list(list_of_prod_obj):
        print("******* Products: *******")
        for item in list_of_prod_obj:
            print(item.name + ' (' + str(item.price) + ')')
        print("*************************")
        # print()  # Add an extra line for looks

    # Get product data from user
    @staticmethod
    def input_products_to_list(product_object, list_of_prod_obj):
        try:
            product_object.name = str(input('Enter product name: ')).title().strip()
            product_object.price = float(input('Enter ' + product_object.name + ' cost: '))
            list_of_prod_obj.append(product_object)
        except ValueError:
            print("Entry error")
            print('Product\'s price must be a number')
        except Exception as e:
            print("Entry error")
            print(e)
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')  # for testing: evaluating errors
        return list_of_prod_obj, 'Success'

    # Require user input before proceeding
    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
product_objects_lst, status_str = FileProcessor.read_file_data_to_string(file_name=file_name_str, list_of_prod_obj=product_objects_lst)  # WORKING!
# print(status_str)  # testing if method ran
# print(product_objects_lst)  # testing if list contains products objects

while True:
    # Show user a menu of options
    IO.print_menu_options()
    # Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':  # Add a new Task
        IO.print_current_products_in_list(list_of_prod_obj=product_objects_lst)
        IO.input_press_to_continue()
        continue

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':
        product = Product('', 0)
        product_objects_lst, status_str = IO.input_products_to_list(product_object=product, list_of_prod_obj=product_objects_lst)
        IO.input_press_to_continue()
        continue

    # let user save current data to file and exit program
    elif choice_str.strip() == '3':
        product_objects_lst, status_str = FileProcessor.save_data_to_file(file_name=file_name_str, list_of_prod_obj=product_objects_lst) #WORKING!!
        IO.input_press_to_continue()
        print('Goodbye!')
        break

    # let user exit program from menu
    elif choice_str.strip() == '0':
        print('Goodbye!')
        break

    else:
        IO.input_press_to_continue('Please select a menu option from 0 to 3')

# Main Body of Script  ---------------------------------------------------- #

