#3
# As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and 
#   shopping cart object. (Set the shopping cart instance variable equal to a new ShoppingCart object in the 
#   initializer HINT: You will have to import the ShoppingCart class into the customer.py file)
# As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.

# As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this 
#   method you will call the shopping cart’s add product method)
# As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over 
#   the shopping cart’s products list and print each product to the terminal)


from ShoppingCart import ShoppingCart
# customer_cart_product = ShoppingCart()
# customer_cart_product.add_new_products()
# customer_cart_product.items_in_cart() 
# customer_cart_product.total_products()


class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.customer_cart = ShoppingCart()
    
    def add_to_cart(self, products):
        #print(products)
        self.customer_cart.add_new_products(products)

    def view_products_in_cart(self): 
        for products in self.customer_cart.carts_products:
            print(products.name, products.price, products.category)


