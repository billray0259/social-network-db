from pymongo import MongoClient
from .message import Message

class MessageDAO:
    def __init__(self, mongo_uri, db_name):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['messages']

    def create(self, message):
        result = self.collection.insert_one({
            "role": message.role,
            "content": message.content,
            "conversation_id": message.conversation_id,
            "timestamp": message.timestamp
        })
        return result.inserted_id

    def get_all(self, conversation_id):
        cursor = self.collection.find({"conversation_id": conversation_id})
        return [Message(m['_id'], m['role'], m['content'], m['conversation_id'], m['timestamp']) for m in cursor]

    def delete_all(self, conversation_id):
        self.collection.delete_many({"conversation_id": conversation_id})
