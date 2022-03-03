#2
# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list). 
# -Like the cards ex to have an empty list 
# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.
# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list) 
# -Demo vid for wallet is similar! 
# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.
# -self.ShopppingCart = []

class ShoppingCart:
    def __init__(self):
        self.carts_products = []

    def total_products(self):
        total = 0
        #self.carts_products = 0
        for products in self.carts_products:
            total += products.price
        return total 

    def add_new_products(self, products):
        self.carts_products.append(products) 

        # self.carts_products += (self.carts_products).append('')
        # self.carts_products += add_product
        # add_product = (self.carts_products).append()

    def empty_cart(self):
        self.carts_products = []
        # self.carts_products -= delete_all_items
        # delete_all_items = (self.carts_products).clear()

