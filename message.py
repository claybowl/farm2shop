from datetime import datetime

class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.now()

    def send_message(self):
        # Logic to send a message
        pass

    def get_messages(self):
        # Logic to retrieve messages
        pass
