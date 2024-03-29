#This is 10.19 ZyBooks
#David Coronado: People Soft ID: 1971072
class ItemToPurchase:

    # Parameter Constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Implement the method
    def print_item_cost(self):
        # print the output in a specifed format
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                            (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Implement the method print_item_description
    def print_item_description(self):
        string = '{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity)
        print(string)
        return string


# Declare the class ShoppingCart
class ShoppingCart:

    # Parameter Constructor
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Implement method to add item in the shopping cart
    def add_item(self):
        print('ADD ITEM TO CART')
        item_name = str(input('Enter the item name:'))
        item_description = str(input('Enter the item description:'))
        item_price = int(input('Enter the item price:'))
        item_quantity = int(input('Enter the item quantity:'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    # Implement the method to delete the item in the cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART')

        string = str(input('Enter name of item to remove:'))
        i = 0

        for item in self.cart_items:
            if (item.item_name == string):
                del self.cart_items[i]
                flag = True
                break

            else:
                flag = False
            i += 1

        if (flag == False):
            # print the message
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')

        name = str(input('Enter the item name:'))
        print()

        for item in self.cart_items:
            if (item.item_name == name):
                quantity = int(input('Enter the new quantity:'))
                item.item_quantity = quantity
                flag = True
                break

            else:
                flag = False

        if (flag == False):
            print('Item not found in cart. Nothing modified.')
        print()

    # implement method to process total number of items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity

        return num_items

    # Implement the method
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0

        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost

        return total_cost

    # Implement the method to print the total
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # Implement the method to print_descriptions
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')

        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    # Implement the method output_cart()
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price)))
            tc += (item.item_quantity * item.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()

        print('Total: ${}'.format(tc))


# Implement the method print_menu
def print_menu(customer_Cart):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    command = ''

    while (command != 'q'):
        print(menu)

        command = input('Choose an option:\n')
        while (command != 'a' and command != 'o' and command != 'i' and command != 'r'
               and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')

        # If the input command is a
        if (command == 'a'):
            customer_Cart.add_item()

        # If the input command is o
        if (command == 'o'):
            customer_Cart.output_cart()

        # If the input command is i
        if (command == 'i'):
            customer_Cart.print_descriptions()

        # If the input command is r
        if (command == 'r'):
            customer_Cart.remove_item()
        if (command == 'c'):
            customer_Cart.modify_item()


def main():
    customer_name = str(input('Enter customer\'s name:\n'))
    current_date = str(input('Enter today\'s date:\n'))
    print('\nCustomer name:', customer_name)
    print('Today\'s date:', current_date)
    x = ShoppingCart(customer_name, current_date)
    print_menu(x)


if __name__ == '__main__':
    main()
