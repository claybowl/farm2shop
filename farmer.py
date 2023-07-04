from user import User

class Farmer(User):
    def __init__(self, name, location, contact_details):
        super().__init__(name, location, contact_details)
        self.products_offered = []

    def list_product(self, product):
        # Logic to list a product
        pass

    def update_product(self, product):
        # Logic to update a product
        pass

    def get_products(self):
        # Logic to retrieve all products offered by the farmer
        pass
