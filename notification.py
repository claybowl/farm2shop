from datetime import datetime

class Notification:
    def __init__(self, recipient, content):
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.now()

    def send_notification(self):
        # Logic to send a notification
        pass

    def get_notifications(self):
        # Logic to retrieve notifications
        pass
