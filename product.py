from dataclasses import dataclass

@dataclass
class Product:
    details: str
    price: float
    availability: bool

    def create_listing(self):
        # Logic to create a product listing
        pass

    def update_listing(self):
        # Logic to update a product listing
        pass

    def get_listing(self):
        # Logic to retrieve a product listing
        pass
