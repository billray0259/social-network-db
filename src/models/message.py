from datetime import datetime

class Message:
    def __init__(self, id, role, content, conversation_id, timestamp=None):
        self.id = id
        self.role = role
        self.content = content
        self.conversation_id = conversation_id
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "conversation_id": self.conversation_id,
            "timestamp": self.timestamp
        }


    def __str__(self):
        return str(self.to_dict())