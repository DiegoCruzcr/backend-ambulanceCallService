import pymongo
from src.domain.models.task import Task

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
            result = collection.find_one({'ambulance_id': ambulance_call_id})
            r = {k: v for k, v in result.items() if k != '_id'}
            return r 
            
    def find_all(self):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            cursor = collection.find({}, projection={'_id': False})
            result = [r for r in cursor]
            return result

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
    
    def create_task(self, task: Task):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            return collection.insert_one(task.to_dict()).inserted_id
        
    def list_tasks(self):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            cursor = collection.find({}, projection={'_id': False})
            result = [r for r in cursor]
            return result
        
    def get_task(self, task_id):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            result = collection.find_one({'task_id': task_id})
            r = {k: v for k, v in result.items() if k != '_id'}
            return r
        
    def update_task(self, task_id, task: Task):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            
            # Create a dictionary representation of the Task object
            task_dict = task.to_dict()

            # Update the document with both associated_users and other fields
            update_data = {
                '$push': {
                    'associated_users': {
                        '$each': task_dict['associated_users']
                    }
                },
                '$set': {
                    'task_image_url': task_dict['task_image_url'],
                    'task_name': task_dict['task_name'],
                    'task_description': task_dict['task_description'],
                    'updated_at': task_dict['updated_at']
                }
            }

            # Update the document using the positional $ operator for the associated_users array
            return collection.update_one({'task_id': task_id}, update_data).modified_count
            
    def delete_task(self, task_id):
        pass
        
    def signUpCompany(self, body):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            
            result = collection.insert_one(body).inserted_id
            print(result)
            return result
        
    def signUpUser(self, body):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            
            return collection.insert_one(body).inserted_id
        
    def getCompany(self, body):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            result = collection.find_one({'company_name': body['company_name']})
            r = {k: v for k, v in result.items() if k != '_id'}
            return r
        
    def getUser(self, body):
        with self as client:
            db = client[self._config['MONGO_DB']]
            collection = db[self._config['MONGO_COLLECTION']]
            result = collection.find_one({'user_name': body['user_name']})
            r = {k: v for k, v in result.items() if k != '_id'}
            return r

    # def get_task_by_associated_user_id(self, user_id):
    #     with self as client:
    #         db = client[self._config['MONGO_DB']]
    #         collection = db[self._config['MONGO_COLLECTION']]
    #         result = 
    #         r = {k: v for k, v in result.items() if k != '_id'}
    #         return r