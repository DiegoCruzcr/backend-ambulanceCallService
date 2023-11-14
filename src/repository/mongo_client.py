import pymongo

from src.repository.database import Database


class MongoClient(Database):
    def __init__(self, config):
        self._config = config
        self._client = None

    def __enter__(self):
        self._client = pymongo.MongoClient(self._config['MONGO_URI'])
        return self._client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()

    def save(self, ambulance_call):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.insert_one(ambulance_call.to_dict()).inserted_id
        
    def find_by_id(self, ambulance_call_id):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.find_one({'ambulance_id': ambulance_call_id})
        
    def find_all(self):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.find({})
        
    def delete(self, ambulance_call_id):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.delete_one({'ambulance_id': ambulance_call_id}).deleted_count
        
    def update(self, ambulance_call_id, ambulance_call):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.update_one({'ambulance_id': ambulance_call_id}, {'$set': ambulance_call.to_dict()}).modified_count
    