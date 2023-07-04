from dataclasses import dataclass

@dataclass
class User:
    name: str
    location: str
    contact_details: str

    def create_profile(self):
        # Logic to create a user profile
        pass

    def update_profile(self):
        # Logic to update a user profile
        pass

    def get_profile(self):
        # Logic to retrieve a user profile
        pass
