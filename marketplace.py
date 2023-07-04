#!/usr/bin/env python3
"""module marketplace
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Marketplace:
    def __init__(self):
        self.cart = []
        self.wishlist = []

    def add_to_cart(self, product):
        # Logic to add a product to the cart
        self.cart.append(product)
        print(f"{product.name} has been added to the cart.")

    def remove_from_cart(self, product):
        # Logic to remove a product from the cart
        if product in self.cart:
            self.cart.remove(product)
            print(f"{product.name} has been removed from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def checkout(self):
        # Logic to complete the checkout process
        total = sum(product.price for product in self.cart)
        print(f"Checkout complete. Total amount: ${total:.2f}")
        self.cart.clear()

    def get_cart(self):
        # Logic to retrieve the cart
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for product in self.cart:
                print(f"- {product.name} (${product.price:.2f})")

    def add_to_wishlist(self, product):
        # Logic to add a product to the wishlist
        self.wishlist.append(product)
        print(f"{product.name} has been added to the wishlist.")

    def remove_from_wishlist(self, product):
        # Logic to remove a product from the wishlist
        if product in self.wishlist:
            self.wishlist.remove(product)
            print(f"{product.name} has been removed from the wishlist.")
        else:
            print(f"{product.name} is not in the wishlist.")

    def get_wishlist(self):
        # Logic to retrieve the wishlist
        if not self.wishlist:
            print("The wishlist is empty.")
        else:
            print("Wishlist contents:")
            for product in self.wishlist:
                print(f"- {product.name} (${product.price:.2f})")


# Example usage:
marketplace = Marketplace()

# Creating products
product1 = Product("Cannabis Strain A", 10.00)
product2 = Product("Cannabis Strain B", 15.00)

# Adding products to cart
marketplace.add_to_cart(product1)
marketplace.add_to_cart(product2)

# Viewing cart
marketplace.get_cart()

# Removing product from cart
marketplace.remove_from_cart(product1)

# Adding product to wishlist
marketplace.add_to_wishlist(product1)

# Viewing wishlist
marketplace.get_wishlist()

# Checkout
marketplace.checkout()
