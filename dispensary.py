from user import User

class Dispensary(User):
    def __init__(self, name, location, contact_details):
        super().__init__(name, location, contact_details)
        self.preferences = {}

    def update_preferences(self, preferences):
        # Logic to update preferences
        pass

    def get_preferences(self):
        # Logic to retrieve preferences
        pass
